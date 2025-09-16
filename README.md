# Desenvolvimento de Sistemas: Web, Desktop e Mobile

## 📖 Introdução
Este documento foi criado como parte da atividade **"Criando README – Web, Desktop e Mobile"**.  
Seu objetivo é apresentar as diferenças entre os principais tipos de desenvolvimento de software (**Web, Desktop e Mobile**), destacando suas características, ferramentas, vantagens e limitações.  

Além disso, o README descreve um **projeto Django (Web)** desenvolvido pelo grupo, explicando como executá-lo e quais funcionalidades ele oferece.  
Compreender esses ambientes é fundamental para **manutenção e atualização** de sistemas, já que cada tipo de software tem necessidades distintas.

---

## 🌐 Desenvolvimento Web
### O que é?
O **desenvolvimento web** consiste na criação de sites e aplicações acessadas por navegadores, podendo rodar em qualquer dispositivo conectado à internet.

### Linguagens e Frameworks
- **Linguagens:** HTML, CSS, JavaScript, Python, PHP  
- **Frameworks:** Django, React, Angular, Vue.js  

### Ferramentas Usadas
- **Visual Studio Code**  
- **Navegadores** (Google Chrome, Firefox, Edge)  
- **Git/GitHub** para versionamento  

### Exemplos
- **E-commerces** (Amazon, Mercado Livre)  
- **Redes sociais** (Instagram Web, Facebook)  
- **Sistemas desenvolvidos em Django**  

### Vantagens
- Acessível em qualquer navegador  
- Atualizações centralizadas no servidor  
- Fácil distribuição  

### Limitações
- Depende de internet  
- Diferenças de compatibilidade entre navegadores  
- Performance inferior a apps nativos  

---

## 💻 Desenvolvimento Desktop
### O que é?
O desenvolvimento Desktop refere-se a aplicativos instalados no computador, funcionando mesmo sem internet.

### Linguagens Comuns
- C#, Java, Python, C++  

### IDEs
- Visual Studio, Eclipse, PyCharm  

### Exemplos
- **Microsoft Office**  
- **Adobe Photoshop**  
- **VLC Media Player**  

### Vantagens
- Melhor desempenho  
- Funciona offline  
- Maior controle de recursos do sistema  

### Limitações
- Dependência do sistema operacional  
- Atualizações menos práticas  
- Menor portabilidade  

---

## 📱 Desenvolvimento Mobile
### O que é?
É o desenvolvimento de aplicativos para smartphones e tablets, essenciais no cenário atual de mobilidade.

### Tipos de Aplicativos
- **Nativos** → desenvolvidos especificamente para iOS ou Android.  
- **Híbridos** → um único código para múltiplas plataformas.  
- **PWAs** → apps baseados na web que se comportam como aplicativos.  

### Frameworks e Ferramentas
- **Android Studio, Xcode**  
- **React Native, Flutter, Ionic**  

### Exemplos
- **WhatsApp, TikTok, Uber**  

### Vantagens
- Grande alcance de usuários  
- Acesso aos recursos do dispositivo (GPS, câmera, notificações)  
- Melhor engajamento  

### Limitações
- Restrições das lojas de aplicativos  
- Fragmentação de dispositivos  
- Atualizações constantes necessárias  

---

## 🔍 Comparação Web, Desktop e Mobile

| Característica       | Web 🌐                         | Desktop 💻                  | Mobile 📱                        |
|----------------------|--------------------------------|-----------------------------|----------------------------------|
| **Acesso**           | Navegador + internet           | Instalado no PC             | Instalado via app store          |
| **Atualizações**     | No servidor (automáticas)      | Requer reinstalação         | Feitas pelas lojas/app stores    |
| **Portabilidade**    | Alta (qualquer navegador)      | Baixa (depende do SO)       | Alta (iOS e Android)             |
| **Exemplos**         | Amazon, Instagram Web          | Photoshop, Office           | WhatsApp, Uber                   |
| **Vantagem Principal** | Fácil acesso                  | Desempenho e offline        | Mobilidade e engajamento         |
| **Limitação**        | Depende da internet/navegador  | Pouca portabilidade         | Fragmentação e restrições        |

---

## 📂 Projeto Django – Padaria Nivus
### 📌 Descrição
O projeto **Padaria Nivus** é uma aplicação **Web** desenvolvida em **Django** para gerenciar **encomendas** de produtos de padaria.  

### ⚙️ Funcionalidades
- Cadastro de encomendas  
- Listagem e gerenciamento  
- Banco de dados SQLite embutido  

### 🚀 Como Executar
1. Clonar o repositório ou extrair os arquivos.  
2. Entrar na pasta `dev2/padaria_nivus`.  
3. Instalar as dependências:  
   ```bash
   pip install django
