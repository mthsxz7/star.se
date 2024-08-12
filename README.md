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
   

# Guia de Contribuição

Obrigado por considerar contribuir para o **STAR.SE**! Ao contribuir, você ajuda a melhorar este projeto e a torná-lo mais útil para todos.

## Como Contribuir

Siga estas etapas para começar a contribuir:

### 1. Faça um Fork do Repositório

Clique no botão "Fork" no canto superior direito da página do repositório para criar uma cópia do projeto em seu GitHub.

### 2. Clone o Repositório

Clone o repositório para o seu ambiente local usando o comando abaixo:

```bash
git clone https://github.com/seu-usuario/star.se.git
cd star.se
```

### 3. Crie um Branch para sua Contribuição

Crie um branch específico para a funcionalidade ou correção que você deseja adicionar:

```bash
git checkout -b minha-contribuicao
```

### 4. Faça as Alterações Necessárias

Implemente suas melhorias ou correções no código. Certifique-se de seguir os padrões de código e práticas recomendadas.

### 5. Faça Commit das Alterações

Depois de concluir suas alterações, faça o commit delas:

```bash
git add .
git commit -m "Descrição clara e concisa do que foi alterado"
```

### 6. Envie o Branch para o Repositório Remoto

Envie suas alterações para o repositório remoto:

```bash
git push origin minha-contribuicao
```

### 7. Abra um Pull Request

Vá até a página do repositório original no GitHub e clique no botão "Compare & Pull Request". Descreva suas alterações e envie o Pull Request.

## Revisão de Código

Todo o código enviado passará por uma revisão antes de ser incorporado ao projeto. Certifique-se de que suas contribuições:

- Sigam o padrão de código do projeto.
- Incluam testes adequados.
- Sejam acompanhadas por documentação, se necessário.

## Agradecimentos

Agradecemos por dedicar seu tempo e esforço para contribuir com o **STAR.SE**! Suas contribuições são valiosas para o crescimento deste projeto.


