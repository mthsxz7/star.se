# STAR.SE

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2%2B-green)](https://www.djangoproject.com/)

## Visão Geral

**STAR.SE** é um sistema robusto e completo, desenvolvido com Python e Django, projetado para conectar startups a investidores. O objetivo principal é facilitar e gerenciar o processo de investimento em startups, desde a apresentação até a conclusão do investimento.

## Funcionalidades

O sistema STAR.SE será desenvolvido com as seguintes funcionalidades principais:

- **Autenticação de Usuários**: Cadastro e login seguro para investidores e startups.
- **Cadastro de Empresas**: Sistema para startups cadastrarem seus dados, como CNPJ, tempo de existência, descrição do negócio, entre outros.
- **Assinatura de Contrato**: Interface para a assinatura de contratos digitais entre startups e investidores.
- **Realização de Investimentos**: Módulo que permite aos investidores realizarem aportes financeiros nas startups de seu interesse.
- **Upload de Documentos**: Sistema de upload para documentos importantes, como contratos, propostas de investimento e relatórios financeiros.
- **Análise de Métricas**: Ferramenta para analisar o desempenho das startups por meio de diversas métricas.
- **Dashboards**: Visualização gráfica e intuitiva dos dados, tanto para investidores quanto para as startups.

## Instalação

1. Clone o repositório e navegue até a pasta do projeto:
   ```bash
   git clone https://github.com/mthsxz7/star.se.git
   cd star.se
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
