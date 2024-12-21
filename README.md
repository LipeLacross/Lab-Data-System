## 🌐 [English Version of README](README_EN.md)

# Sistema de Gerenciamento de Qualidade da Água

Este projeto é uma aplicação web desenvolvida em Flask para gerenciar dados de qualidade da água. Ele permite o cadastro e autenticação de usuários com diferentes níveis de acesso (admin e operador), a gestão de estações de monitoramento e a inserção e visualização de análises de parâmetros como DBO, DQO e pH.

## 🔨 Funcionalidades do Projeto

- **Autenticação de Usuários**: Registro e login de usuários com roles distintas (admin e operador).
- **Gestão de Estações**: Adição e visualização de estações de monitoramento de qualidade da água.
- **Gestão de Usuários**: Admins podem adicionar novos usuários com diferentes roles.
- **Inserção de Análises**: Operadores podem inserir dados de análises de qualidade da água.
- **Visualização de Dados**: Visualização de dados históricos de análises para cada estação.
- **Dashboards Personalizados**: Interfaces distintas para administradores e operadores.

### Exemplo Visual do Projeto



## ✔️ Técnicas e Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Flask
- **Banco de Dados**: SQLite com SQLAlchemy
- **Autenticação**: JWT (JSON Web Tokens)
- **Frontend**: HTML, CSS (com estilização básica)
- **Templates**: Jinja2
- **Outras Bibliotecas**:
  - `flask_jwt_extended` para gerenciamento de tokens JWT
  - `flask_sqlalchemy` para ORM

## 📁 Estrutura do Projeto

```
├── LICENSE
├── anotations.txt
├── app.py
├── static/
│   ├── style.css
│   └── images/
│       ├── dashboard_admin.png
│       └── dashboard_operator.png
└── templates/
├── dashboard_admin.html
├── dashboard_operator.html
├──login.html
├── README.md
└── README_EN.md
```

- **LICENSE**: Arquivo de licença do projeto.
- **anotations.txt**: Possivelmente para anotações ou documentação adicional.
- **app.py**: Arquivo principal da aplicação Flask contendo rotas, modelos e lógica de negócio.
- **static/**: Diretório para arquivos estáticos como CSS e imagens.
  - **style.css**: Folha de estilos para o frontend.
  - **images/**: Imagens utilizadas nos templates (exemplos visuais).
- **templates/**: Diretório para templates HTML renderizados pelo Flask.
  - **dashboard_admin.html**: Interface para administradores.
  - **dashboard_operator.html**: Interface para operadores.
  - **login.html**: Página de login.

## 🛠️ Abrir e rodar o projeto

Para iniciar o projeto localmente, siga os passos abaixo:

1. **Certifique-se de que o Python está instalado**:
   - O [Python](https://www.python.org/) é necessário para rodar o projeto. Você pode verificar se já o tem instalado com:
     
     ```bash
     python --version
     ```

   - Se não estiver instalado, baixe e instale a versão recomendada.

2. **Clone o Repositório**:
   - Copie a URL do repositório e execute o comando abaixo no terminal:
     
     ```bash
     git clone <URL_DO_REPOSITORIO>
     ```

3. **Navegue até o diretório do projeto**:
   
   ```bash
   cd <NOME_DO_DIRETORIO>
   ```

4. **Crie um ambiente virtual** (recomendado):

   ```bash
   python -m venv venv
   ```

5. **Ative o ambiente virtual**:
    - **No Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - **No macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

6. **Instale as dependências**:
    - Caso não exista um arquivo `requirements.txt`, crie-o com as seguintes dependências:

      ```
      Flask
      Flask_SQLAlchemy
      Flask_JWT_Extended
      ```

    - Então, instale as dependências com:

      ```bash
      pip install -r requirements.txt
      ```

7. **Configure as variáveis de ambiente** (opcional):
    - Você pode definir variáveis como `SECRET_KEY` ou configurações específicas se necessário.

8. **Inicialize o banco de dados**:
    - Execute o aplicativo uma vez para criar as tabelas do banco de dados:

      ```bash
      python app.py
      ```

    - Após a execução inicial, você pode parar o servidor (`Ctrl+C`).

9. **Rodar o aplicativo**:

   ```bash
   python app.py
   ```

    - A aplicação estará disponível em `http://127.0.0.1:5000/`.

## 🌐 Deploy

Para fazer o deploy da aplicação, você pode utilizar plataformas como **Heroku**, **Render**, ou **DigitalOcean**. A seguir, um guia básico para deploy no Heroku:

1. **Instale a CLI do Heroku**:
    - [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) é necessária para interagir com a plataforma.

2. **Faça login no Heroku**:

   ```bash
   heroku login
   ```

3. **Crie um novo aplicativo no Heroku**:

   ```bash
   heroku create nome-do-seu-app
   ```

4. **Adicione um `Procfile`**:
    - Crie um arquivo chamado `Procfile` na raiz do projeto com o seguinte conteúdo:

      ```
      web: python app.py
      ```

5. **Faça commit e envie para o Heroku**:

   ```bash
   git add .
   git commit -m "Deploy para Heroku"
   git push heroku main
   ```

6. **Configure as variáveis de ambiente no Heroku**:
    - Defina o `SECRET_KEY` e outras configurações necessárias através do dashboard do Heroku ou via CLI:

      ```bash
      heroku config:set SECRET_KEY='sua_chave_secreta'
      ```

7. **Acesse o aplicativo**:
    - Após o deploy bem-sucedido, o aplicativo estará disponível no URL fornecido pelo Heroku.

