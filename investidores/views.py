from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal, InvalidOperation
from django.http import Http404
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages import constants
from empresarios.models import Empresas, Documento
from .models import PropostaInvestimento

def sugestao(request):
    if not request.user.is_authenticated:
        return redirect('usuarios:logar')  # Use o nome da URL para maior flexibilidade
    
    areas = Empresas.area_choices
    
    if request.method == "GET":
        return render(request, 'sugestao.html', {'areas': areas})
    
    elif request.method == "POST":
        tipo = request.POST.get('tipo')
        area = request.POST.getlist('area')
        valor = request.POST.get('valor')

        tipo_opcoes = {
            'C': Q(tempo_existencia__gte=5) & Q(estagio="E"),
            'D': Q(tempo_existencia__in=['-6', '+6', '+1']) & ~Q(estagio="E"),
            'G': Q(),  # Para o tipo genérico, você pode querer todos os registros
        }

        empresas = Empresas.objects.filter(tipo_opcoes[tipo])
        empresas = empresas.filter(area__in=area)

        empresas_selecionadas = []
        for empresa in empresas:
            try:
                percentual = (Decimal(valor) * 100) / Decimal(empresa.valuation)
                if percentual >= 1:
                    empresas_selecionadas.append(empresa)
            except (ValueError, ZeroDivisionError, InvalidOperation):
                continue

        return render(request, 'sugestao.html', {'empresas': empresas_selecionadas, 'areas': areas})

def ver_empresa(request, id):
    empresa = get_object_or_404(Empresas, id=id)
    documentos = Documento.objects.filter(empresa=empresa)
    proposta_investimentos = PropostaInvestimento.objects.filter(empresa=empresa).filter(status='PA')
    percentual_vendido = 0
    for pi in proposta_investimentos:
        percentual_vendido = percentual_vendido + pi.percentual
        
    limiar = (80 * empresa.percentual_equity) / 100
    concretizado = False
    if percentual_vendido >= limiar:
        concretizado = True
    
    percentual_disponivel = empresa.percentual_equity - percentual_vendido

    
    return render(request, 'ver_empresa.html', {'empresa': empresa, 'documentos': documentos, 'percetual_vendido': int(percentual_vendido), 'concretizado': concretizado,'percentual_disponivel': percentual_disponivel})

def realizar_proposta(request, id):
    valor = request.POST.get('valor')
    percentual = request.POST.get('percentual')
    empresa = Empresas.objects.get(id=id)

    try:
        valor_decimal = Decimal(valor)
        percentual_decimal = Decimal(percentual)
    except InvalidOperation:
        messages.add_message(request, constants.WARNING, 'Erro ao converter valor ou percentual para decimal.')
        return redirect(f'/investidores/ver_empresa/{id}')

    propostas_aceitas = PropostaInvestimento.objects.filter(empresa=empresa).filter(status='PA')
    total = Decimal(0)

    for pa in propostas_aceitas:
        total += pa.percentual

    if total + percentual_decimal > empresa.percentual_equity:
        messages.add_message(request, constants.WARNING, 'O percentual solicitado ultrapassa o percentual máximo.')
        return redirect(f'/investidores/ver_empresa/{id}')

    try:
        valuation = (100 * valor_decimal) / percentual_decimal
    except (ValueError, ZeroDivisionError, InvalidOperation):
        messages.add_message(request, constants.WARNING, 'Erro ao calcular o valuation.')
        return redirect(f'/investidores/ver_empresa/{id}')

    if valuation < (Decimal(empresa.valuation) / 2):
        messages.add_message(request, constants.WARNING, f'Seu valuation proposto foi R${valuation} e deve ser no mínimo R${empresa.valuation/2}')
        return redirect(f'/investidores/ver_empresa/{id}')

    pi = PropostaInvestimento(
        valor=valor_decimal,
        percentual=percentual_decimal,
        empresa=empresa,
        investidor=request.user,
    )

    pi.save()

    return redirect(f'/investidores/assinar_contrato/{pi.id}')

def assinar_contrato(request, id):
    pi = get_object_or_404(PropostaInvestimento, id=id)
    
    if pi.status != "AS":
        raise Http404()
    
    if request.method == "GET":
        return render(request, 'assinar_contrato.html', {'id': id, 'pi': pi})
    
    elif request.method == "POST":
        selfie = request.FILES.get('selfie')
        rg = request.FILES.get('rg')

        # Verificar se os arquivos foram enviados
        if selfie and rg:
            pi.selfie = selfie
            pi.rg = rg
            pi.status = 'PE'
            pi.save()
            
            success_message = 'Contrato assinado com sucesso, sua proposta foi enviada à empresa.'
            messages.success(request, success_message)
            return redirect(f'/investidores/ver_empresa/{pi.empresa.id}')