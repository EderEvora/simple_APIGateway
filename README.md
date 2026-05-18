# 📘 API Monolítica – Sistema de loja e-commerce

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
pip install flask requests
```

### 2. Executar a aplicação

```
python app.py
```

> Para escalar, passar a porta como argumento:
> ```
> python app.py 5001
> python app.py 5002
> ```

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

```
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

```
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

### Teste de carga

Para simular múltiplos utilizadores em simultâneo:

```
python teste_carga.py
```

O script cria 50 threads em simultâneo e apresenta no final:
* Total de requisições
* Requisições com sucesso / erro
* Tempo médio de resposta
* Duração total do teste

Para alterar o número de utilizadores, editar a última linha do ficheiro `teste_carga.py`:
```
run_teste(50)  # alterar para o número desejado
```

---
## ⚠️ Limitações

* Dados armazenados apenas em memória (sem base de dados)
* Não possui autenticação
* Tratamento de erros limitado
* Não escalável (característica da arquitetura monolítica)

---
## 🆕 Alterações – Escalabilidade (Trabalho 02)

As seguintes alterações foram feitas no `app.py`:

* A porta passou a ser configurável via argumento no terminal (`sys.argv`)
* Foi adicionado um identificador de instância (`INSTANCE = f"instance-{PORT}"`)
* Todas as respostas passaram a incluir o campo `"instance"` no JSON, para identificar qual instância respondeu

Exemplo de resposta:
```
{
  "instance": "instance-5001",
  "data": [...]
}
```

Foi adicionado o `load_balancer.py` que distribui as requisições entre instâncias usando **round-robin**.

### Executar com escala

```
# Terminal 1
python app.py 5001

# Terminal 2
python app.py 5002

# Terminal 3
python load_balancer.py
```

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
