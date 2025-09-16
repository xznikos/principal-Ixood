# Desenvolvimento de Sistemas: Web, Desktop e Mobile

## 📌 Introdução
Este documento tem como objetivo apresentar uma visão geral dos três principais tipos de desenvolvimento de software: **Web, Desktop e Mobile**. Ele também descreve o projeto **Padaria Nivus**, um sistema desenvolvido em Django para gerenciar encomendas de produtos de padaria.

Compreender as diferenças entre Web, Desktop e Mobile é essencial para escolher a tecnologia certa em cada contexto, garantindo melhor manutenção, desempenho e experiência do usuário.

---

## 🍞 Projeto: Padaria Nivus

### 📝 Descrição
O **Padaria Nivus** é um sistema **Web**, desenvolvido com o framework **Django**, que permite gerenciar **encomendas de produtos de padaria**. Seu objetivo é facilitar o registro, organização e controle de pedidos, oferecendo praticidade tanto para o administrador quanto para os clientes.

### ⚙️ Funcionalidades
- Cadastro e listagem de encomendas
- Gerenciamento de produtos (ex: lasanha, pão de queijo, doces)
- Área administrativa integrada com o Django Admin
- Armazenamento de dados em banco de dados **SQLite**

### 📂 Estrutura principal do projeto
- `dev2/padaria_nivus/` → Código principal do sistema Django
- `encomendas/` → Aplicação responsável pelo controle de pedidos
- `db.sqlite3` → Banco de dados local
- `static/` e `media/` → Arquivos estáticos e imagens dos produtos

### 🚀 Como executar o projeto
1. Clone o repositório no GitHub
   ```bash
   git clone <url-do-seu-repositorio>
   cd padaria_nivus

2. Crie e ative um ambiente virtual.
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. Instale as dependências
   ```bash
   pip install -r requirement.txt

4. Execute as migrações
   ```bash
   python manage.py migrate

5. Inicie o servidor
   ```bash
   python manage.py runserver

6. Acesse o navegador
7. ```bash  
   http://127.0.0.1:8000
