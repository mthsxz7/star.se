from django.shortcuts import render, redirect
from .models import Empresas, Documento, Metricas
from django.contrib import messages
from django.contrib.messages import constants
from django.http import Http404
import logging

logger = logging.getLogger(__name__)

def validar_campos_obrigatorios(dados, campos_obrigatorios):
    erros = {}
    for campo in campos_obrigatorios:
        if not dados.get(campo):
            erros[campo] = "Campo obrigatório."
    return erros

def cadastrar_empresa(request):
    if not request.user.is_authenticated:
        return redirect('logar')

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
            'estagio': request.POST.getlist('estagio'),  # Manejo de checkboxes
            'area': request.POST.get('area'),
            'publico_alvo': request.POST.get('publico_alvo'),
            'valor': request.POST.get('valor')
        }
        pitch = request.FILES.get('pitch')
        logo = request.FILES.get('logo')

        campos_obrigatorios = [
            'nome', 'cnpj', 'tempo_existencia', 'descricao',
            'data_final', 'percentual_equity', 'estagio', 'area',
            'publico_alvo', 'valor'
        ]

        erros = validar_campos_obrigatorios(dados, campos_obrigatorios)

        if not pitch:
            erros['pitch'] = 'Campo obrigatório.'
        if not logo:
            erros['logo'] = 'Campo obrigatório.'

        if erros:
            for field, error in erros.items():
                messages.add_message(request, constants.ERROR, f"{field}: {error}")
            return render(request, 'cadastrar_empresa.html', {
                'tempo_existencia': Empresas.tempo_existencia_choices,
                'areas': Empresas.area_choices,
                'errors': erros,
                'dados': request.POST,
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
                estagio=','.join(dados['estagio']),  # Salvando múltiplos valores como uma string
                area=dados['area'],
                publico_alvo=dados['publico_alvo'],
                valor=dados['valor'],
                pitch=pitch,
                logo=logo  # Assume que logo é um arquivo
            )
            empresa.save()
            messages.add_message(request, constants.SUCCESS, 'Empresa criada com sucesso')
            return redirect('/empresarios/cadastrar_empresa')
        except Exception as e:
            logger.error(f"Erro ao cadastrar empresa: {e}")
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema. Tente novamente mais tarde.')
            return render(request, 'cadastrar_empresa.html', {
                'tempo_existencia': Empresas.tempo_existencia_choices,
                'areas': Empresas.area_choices,
                'dados': request.POST,
                'errors': {'internal': 'Erro interno do sistema.'},
            })

def listar_empresas(request):
    if request.method == 'GET':
        empresas = Empresas.objects.filter(user=request.user)
        return render(request, 'listar_empresas.html', {'empresas': empresas})

def empresas(request, id):
    if empresa.user != request.user:
        messages.add_message(request, constants.ERROR, "Esta não é sua empresa.")
        return redirect(f'/empresarios/listar_empresas')
    try:
        empresa = Empresas.objects.get(id=id, user=request.user)
    except Empresas.DoesNotExist:
        raise Http404('Empresa não encontrada')

    if request.method == "GET":
        documentos = Documento.objects.filter(empresa=empresa)
        return render(request, 'empresa.html', {'empresa': empresa, 'documentos': documentos})
    
def add_doc(request, id):
    try:
        empresa = Empresas.objects.get(id=id, user=request.user)
    except Empresas.DoesNotExist:
        messages.add_message(request, constants.ERROR, "Empresa não encontrada.")
        return redirect(f'/empresarios/listar_empresas')

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        arquivo = request.FILES.get('arquivo')

        if not arquivo:
            messages.add_message(request, constants.ERROR, "Envie um arquivo.")
            return redirect(f'/empresarios/empresa/{id}')

        if not arquivo.name.endswith('.pdf'):
            messages.add_message(request, constants.ERROR, "Envie apenas PDF's.")
            return redirect(f'/empresarios/empresa/{id}')

        documento = Documento(
            empresa=empresa,
            titulo=titulo,
            arquivo=arquivo
        )
        documento.save()
        messages.add_message(request, constants.SUCCESS, "Arquivo cadastrado com sucesso.")
        return redirect(f'/empresarios/empresa/{id}')


def excluir_dc(request, id):
    try:
        documento = Documento.objects.get(id=id)
        if documento.empresa.user != request.user:
            messages.add_message(request, constants.ERROR, "Esse documento não é seu.")
            return redirect(f'/empresarios/empresa/{documento.empresa.id}')

        documento.delete()
        messages.add_message(request, constants.SUCCESS, "Documento excluído com sucesso.")
        return redirect(f'/empresarios/empresa/{documento.empresa.id}')
    except Documento.DoesNotExist:
        messages.add_message(request, constants.ERROR, "Documento não encontrado.")
        return redirect('/empresarios/listar_empresas')


def add_metrica(request, id):
    try:
        empresa = Empresas.objects.get(id=id, user=request.user)
    except Empresas.DoesNotExist:
        messages.add_message(request, constants.ERROR, "Empresa não encontrada.")
        return redirect(f'/empresarios/listar_empresas')

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        valor = request.POST.get('valor')

        if not titulo or not valor:
            messages.add_message(request, constants.ERROR, "Título e valor são obrigatórios.")
            return redirect(f'/empresarios/empresa/{id}')

        metrica = Metricas(
            empresa=empresa,
            titulo=titulo,
            valor=valor
        )
        metrica.save()
        messages.add_message(request, constants.SUCCESS, "Métrica cadastrada com sucesso.")
        return redirect(f'/empresarios/empresa/{id}')

