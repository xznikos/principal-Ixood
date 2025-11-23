# Desenvolvimento de Sistemas: Web, Desktop e Mobile

## 📌 Introdução
Este documento tem como objetivo apresentar uma visão geral dos três principais tipos de desenvolvimento de software: **Web, Desktop e Mobile**. Ele também descreve o projeto **Padaria Nivus**, um sistema desenvolvido em Django para gerenciar encomendas de produtos de padaria.

Compreender as diferenças entre Web, Desktop e Mobile é essencial para escolher a tecnologia certa em cada contexto, garantindo melhor manutenção, desempenho e experiência do usuário.

---

## 🍞 Projeto: Padaria Nivus

### 📝 Descrição
O **Ixood** é um sistema **Web**, desenvolvido com o framework **Django**, que permite gerenciar **encomendas de produtos**. Seu objetivo é facilitar o registro, organização e controle de pedidos, oferecendo praticidade tanto para o administrador quanto para os clientes.

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
    ```bash  
   http://127.0.0.1:8000

## 🌐 Desenvolvimento Web

### O que é?
Desenvolvimento de aplicações acessíveis via navegadores (sites, sistemas online, portais).

### Linguagens e frameworks principais:
- **HTML, CSS, JavaScript**
- **Frameworks:** React, Angular, Vue.js
- **Backend:** Django, Flask, Node.js

### Ferramentas comuns:
VS Code, navegadores, Postman.

### Exemplos de projetos:
Google, Facebook, sistemas de e-commerce.

### Vantagens:
Acessibilidade, multiplataforma, fácil atualização.

### Limitações:
Depende de internet, problemas de compatibilidade entre navegadores.

---

## 💻 Desenvolvimento Desktop

### O que é?
Criação de softwares que rodam diretamente em computadores pessoais (Windows, Linux, macOS).

### Linguagens comuns:
C#, Java, Python, C++.

### IDEs usadas:
Visual Studio, Eclipse, PyCharm.

### Exemplos:
Microsoft Office, Adobe Photoshop.

### Vantagens:
Maior desempenho, acesso offline, integração direta com hardware.

### Limitações:
Dependência de sistema operacional, atualizações mais complexas.

---

## 📱 Desenvolvimento Mobile

### O que é?
Desenvolvimento de aplicativos para smartphones e tablets.

### Tipos de apps:
- **Nativos:** feitos para Android (Java/Kotlin) ou iOS (Swift).
- **Híbridos:** um único código para várias plataformas (ex: Ionic, Cordova).
- **PWAs:** aplicativos progressivos que rodam no navegador como apps.

### Ferramentas/Frameworks:
Flutter, React Native, Android Studio, Xcode.

### Exemplos práticos:
WhatsApp, Instagram, Uber.

### Vantagens:
Grande engajamento, uso de recursos do dispositivo (GPS, câmera).

### Limitações:
Dependência das lojas de aplicativos, fragmentação de dispositivos.

---

## 📊 Comparação entre Web, Desktop e Mobile

| Aspecto | Web 🌐 | Desktop 💻 | Mobile 📱 |
| :--- | :--- | :--- | :--- |
| **Plataforma** | Navegadores | Computadores | Smartphones/Tablets |
| **Acesso** | Online | Offline | Online/Offline |
| **Atualizações** | Imediatas no servidor | Precisa reinstalar | Via lojas de apps |
| **Exemplos** | E-commerce | Photoshop | WhatsApp |
| **Linguagens comuns**| HTML, CSS, JS, Python | C#, Java, Python | Kotlin, Swift, Dart |
| **Vantagens** | Acessibilidade | Desempenho | Engajamento |
| **Limitações** | Internet | Plataforma | Restrições da loja |

---

## ✅ Conclusão

Durante a criação deste README, foi possível entender as diferenças e aplicações entre os tipos de desenvolvimento: Web, Desktop e Mobile. O projeto Padaria Nivus exemplifica o desenvolvimento Web, mostrando como frameworks como o Django podem ser usados para criar sistemas práticos de gestão e manutenção.

Esse entendimento ajuda na escolha da tecnologia ideal para cada situação e amplia a visão sobre manutenção, atualização e usabilidade de softwares.

---

## 👥 Membros do grupo
- Níkolas
