# 📘 API Monolítica – Sistema de Loja

## 📌 Descrição

Este projeto consiste em uma **API monolítica desenvolvida em Python utilizando Flask**, que simula um sistema simples de loja (e-commerce).

A aplicação centraliza todas as funcionalidades em um único sistema, incluindo:

* Gestão de utilizadores
* Gestão de produtos
* Gestão de pedidos

---

## 🧱 Arquitetura

Este projeto segue o modelo de **arquitetura monolítica**, onde:

* Todas as funcionalidades estão integradas em uma única aplicação
* Existe um único ponto de entrada
* Não há separação em serviços independentes

---

## 🛠️ Tecnologias Utilizadas

* Python
* Flask
* JSON (armazenamento em memória)

---

## 🚀 Como Executar

### 1. Instalar dependências

```bash
pip install flask
```

### 2. Executar a aplicação

```bash
python app.py
```

### 3. Acessar a API

A API estará disponível em:

```
http://localhost:5000
```

---

## 📡 Endpoints

### 👤 Utilizadores

#### 🔹 Listar todos os utilizadores

```
GET /users
```

#### 🔹 Buscar utilizador por ID

```
GET /users/{id}
```

#### 🔹 Criar utilizador

```
POST /users
```

📥 Body (JSON):

```json
{
  "id": 3,
  "name": "Novo Usuario"
}
```

---

### 📦 Produtos

#### 🔹 Listar todos os produtos

```
GET /products
```

#### 🔹 Editar produto

```
PUT /products/{id}
```

📥 Body (JSON):

```json
{
  "price": 20000
}
```

---

### 🛒 Pedidos

#### 🔹 Listar todos os pedidos

```
GET /orders
```

---

## 🧪 Testes

A API pode ser testada utilizando:

* Postman
* Browser (para requisições GET)

---

## ⚠️ Limitações

* Dados armazenados apenas em memória (sem base de dados)
* Não possui autenticação
* Tratamento de erros limitado
* Não escalável (característica da arquitetura monolítica)

---

## 📊 Vantagens

* Simples de desenvolver e testar
* Fácil de entender
* Ideal para projetos pequenos

---

## ❌ Desvantagens

* Difícil de escalar
* Alta dependência entre componentes
* Alterações podem impactar todo o sistema

---

## 👨‍💻 Autor

Projeto desenvolvido para fins académicos.
