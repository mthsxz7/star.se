from django.shortcuts import render, redirect
from .models import Empresas
from django.contrib import messages
from django.contrib.messages import constants

def validar_campos_obrigatorios(dados, campos_obrigatorios):
    erros = {}
    for campo in campos_obrigatorios:
        if not dados.get(campo):
            erros[campo] = "Campo obrigatório."
    return erros

def cadastrar_empresa(request):
    if request.method == "GET":
        return render(request, 'cadastrar_empresa.html', {
            'tempo_existencia': Empresas.tempo_existencia_choices,
            'areas': Empresas.area_choices 
        })

    elif request.method == "POST":
        dados = {
            'nome': request.POST.get('nome'),
            'cnpj': request.POST.get('cnpj'),
            'site': request.POST.get('site'),
            'tempo_existencia': request.POST.get('tempo_existencia'),
            'descricao': request.POST.get('descricao'),
            'data_final': request.POST.get('data_final'),
            'percentual_equity': request.POST.get('percentual_equity'),
            'estagio': request.POST.get('estagio'),
            'area': request.POST.get('area'),
            'publico_alvo': request.POST.get('publico_alvo'),
            'valor': request.POST.get('valor')
        }
        pitch = request.FILES.get('pitch')
        logo = request.FILES.get('logo')
        
        campos_obrigatorios = [
            'nome', 'cnpj', 'site', 'tempo_existencia', 'descricao',
            'data_final', 'percentual_equity', 'estagio', 'area',
            'publico_alvo', 'valor', 'pitch', 'logo'
        ]

        erros = validar_campos_obrigatorios(dados, campos_obrigatorios)

        # Adiciona erro se os campos obrigatórios 'pitch' e 'logo' não forem preenchidos
        if not pitch:
            erros['pitch'] = "Campo obrigatório."
        if not logo:
            erros['logo'] = "Campo obrigatório."

        if erros:
            for field, error in erros.items():
                messages.add_message(request, constants.ERROR, f"{field}: {error}")
            return render(request, 'cadastrar_empresa.html', {
                'tempo_existencia': Empresas.tempo_existencia_choices,
                'areas': Empresas.area_choices,
                'errors': erros,
                'dados': request.POST,  # Retorna os dados preenchidos para não perder o que foi inserido
            })

        try:
            empresa = Empresas(
                user=request.user,
                nome=dados['nome'],
                cnpj=dados['cnpj'],
                site=dados['site'],
                tempo_existencia=dados['tempo_existencia'],
                descricao=dados['descricao'],
                data_final_captacao=dados['data_final'],
                percentual_equity=dados['percentual_equity'],
                estagio=dados['estagio'],
                area=dados['area'],
                publico_alvo=dados['publico_alvo'],
                valor=dados['valor'],
                pitch=pitch,
                logo=logo
            )
            empresa.save()
            messages.add_message(request, constants.SUCCESS, 'Empresa criada com sucesso')
        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro interno do sistema: {e}')
            return redirect('/empresarios/cadastrar_empresa')
        
        return redirect('/empresarios/cadastrar_empresa')
