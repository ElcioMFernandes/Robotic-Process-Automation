# RPA - Monitor e Gerenciador de RPA

Este projeto, temporariamente chamado de **RPA**, é uma aplicação que integra o monitoramento e gerenciamento de automações (RPA - Robotic Process Automation).

O **back-end** utiliza **FastAPI**, **MongoDB** e **APScheduler**, enquanto o **front-end** é desenvolvido com **Next.js**, **TypeScript** e estilizado com **Tailwind CSS**.

---

## 📋 **Requisitos**

Certifique-se de ter instalado em sua máquina:

- **Python** 3.10.11
- **Node.js** (versão LTS recomendada)
- **MongoDB**

---

## 🚀 **Instalação e Configuração**

### 1. **Iniciando o MongoDB**

Abra um terminal e execute o seguinte comando:

```bash
mongod
```

### 2. **Configurando o Back-end**

Abra um segundo terminal e siga os comandos abaixo:

```bash
cd server

# Instale o virtualenv (caso ainda não tenha)
pip install virtualenv

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/MacOS

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor FastAPI
uvicorn main:API --reload
```

> **Nota:** Se ocorrerem problemas com SSL ao usar `pip`, utilize o seguinte comando:
>
> ```bash
> pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
> ```

### 3. **Configurando o Front-end**

Abra um terceiro terminal e execute:

```bash
cd client

# Instale as dependências do Node.js
npm install

# Execute o projeto em desenvolvimento
npm run dev
```

---

## 🛠️ **Instalando o npm sem SSL/TLS**

Se você estiver enfrentando problemas relacionados ao SSL/TLS durante a instalação do npm, utilize o comando abaixo para desabilitar temporariamente a verificação:

```bash
npm config set strict-ssl false
```

Para restaurar a configuração original:

```bash
npm config set strict-ssl true
```

> **Aviso de Segurança**: Desabilitar SSL/TLS não é recomendado em ambientes de produção, pois reduz a segurança das conexões.

---

## 💻 **Execução do Projeto**

Após concluir as configurações acima:

1. Certifique-se de que o **MongoDB** esteja em execução.
2. Ative o **Back-end** com `uvicorn main:API --reload`.
3. Execute o **Front-end** com `npm run dev`.

Acesse o projeto pelo navegador no endereço padrão:

```
http://localhost:3000
```

---

## 📚 **Tecnologias Utilizadas**

- **Back-end:** FastAPI, APScheduler, MongoDB
- **Front-end:** Next.js, TypeScript, Tailwind CSS
- **Outras:** Python, Node.js

---

## 🎯 **Objetivo do Projeto**

O objetivo deste projeto é criar uma aplicação que simplifique o gerenciamento de Robotic Process Automation (RPA), oferecendo uma interface moderna e intuitiva para monitoramento e agendamento das automações.

---

## 🤝 **Contribuindo**

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir **Issues** e enviar **Pull Requests**.

1. Faça um **fork** do projeto.
2. Crie uma **branch** para sua feature/fix:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça suas alterações e **commit**:
   ```bash
   git commit -m "Adiciona nova funcionalidade X"
   ```
4. Faça o **push** para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um **Pull Request**.
