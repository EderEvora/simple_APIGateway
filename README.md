📘 API Monolítica – Sistema de Loja
📌 Descrição
Este projeto consiste em uma API monolítica desenvolvida em Python utilizando Flask, que simula um sistema simples de loja (e-commerce).
A aplicação centraliza todas as funcionalidades em um único sistema, incluindo:

Gestão de utilizadores
Gestão de produtos
Gestão de pedidos


🧱 Arquitetura
Este projeto segue o modelo de arquitetura monolítica, onde:

Todas as funcionalidades estão integradas em uma única aplicação
Existe um único ponto de entrada
Não há separação em serviços independentes


🛠️ Tecnologias Utilizadas

Python
Flask
JSON (armazenamento em memória)


🚀 Como Executar
1. Instalar dependências
bashpip install flask requests
2. Executar a aplicação
bashpython app.py

Para escalar, é possível passar a porta como argumento:
bashpython app.py 5001
python app.py 5002

3. Acessar a API
A API estará disponível em:
http://localhost:5000

📡 Endpoints
👤 Utilizadores
🔹 Listar todos os utilizadores
GET /users
🔹 Buscar utilizador por ID
GET /users/{id}
🔹 Criar utilizador
POST /users
📥 Body (JSON):
json{
  "id": 3,
  "name": "Novo Usuario"
}

📦 Produtos
🔹 Listar todos os produtos
GET /products
🔹 Editar produto
PUT /products/{id}
📥 Body (JSON):
json{
  "price": 20000
}

🛒 Pedidos
🔹 Listar todos os pedidos
GET /orders

🆕 Alterações para Escalabilidade (Trabalho 02)
As seguintes alterações foram feitas no app.py para suportar múltiplas instâncias:

A porta passou a ser configurável via argumento no terminal (sys.argv)
Foi adicionado um identificador de instância (INSTANCE = f"instance-{PORT}")
Todas as respostas passaram a incluir o campo "instance" no JSON, para identificar qual instância respondeu a cada requisição

Exemplo de resposta:
json{
  "instance": "instance-5001",
  "data": [...]
}
Foi também adicionado um load balancer (load_balancer.py) que distribui as requisições entre as instâncias usando round-robin.
Executar com escala
bash# Terminal 1
python app.py 5001

# Terminal 2
python app.py 5002

# Terminal 3
python load_balancer.py

🧪 Testes
A API pode ser testada utilizando:

Postman
Browser (para requisições GET)

Teste de carga
bashpython teste_carga.py

⚠️ Limitações

Dados armazenados apenas em memória (sem base de dados)
Não possui autenticação
Tratamento de erros limitado
Não escalável (característica da arquitetura monolítica)


📊 Vantagens

Simples de desenvolver e testar
Fácil de entender
Ideal para projetos pequenos


❌ Desvantagens

Difícil de escalar
Alta dependência entre componentes
Alterações podem impactar todo o sistema


👨‍💻 Autor
Projeto desenvolvido para fins académicos.