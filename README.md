# projeto-de-PI
# ProgressoFit
Sistema web para praticantes de musculação acompanharem sua evolução corporal e receberem treinos personalizados com apoio de Inteligência Artificial.

## Funcionalidades

- Cadastro e login (e-mail/senha com confirmação obrigatória, e login social via Google)
- Perfil de usuário editável (foto, descrição, nível de conhecimento corporal)
- Registro de métricas corporais (peso, altura, percentual de gordura, circunferências)
- Histórico e gráficos de evolução corporal
- Geração de treino personalizado por IA, a partir de um formulário de anamnese
- Ranking público de medidas corporais, com verificação administrativa
- Cadastro de especialistas (nutricionista, educador físico) com verificação profissional

## Tecnologias utilizadas

- **Backend:** Python 3 / Django 6.1
- **Autenticação:** django-allauth
- **Banco de dados:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript
- **Gráficos:** Chart.js
- **IA:** API da Anthropic (Claude)

## Como executar o projeto localmente

### Pré-requisitos
- Python 3.12 ou superior instalado
- Git instalado

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
