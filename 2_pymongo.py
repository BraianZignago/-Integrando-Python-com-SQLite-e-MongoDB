from pymongo import MongoClient

# Conecte ao MongoDB Atlas usando a string de conexão
client = MongoClient("sua_string_de_conexão")

# Crie ou conecte ao banco de dados
db = client['banco']

# Defina a coleção bank
collection = db['bank']


# Exemplo de documentos a serem inseridos
clientes = [
    {
        "nome": "João Silva",
        "cpf": "123456789",
        "endereco": "Rua A",
        "contas": [
            {"tipo": "corrente", "agencia": "0001", "num": 1234, "saldo": 1000.50},
            {"tipo": "poupança", "agencia": "0001", "num": 5678, "saldo": 2000.75}
        ]
    },
    {
        "nome": "Maria Oliveira",
        "cpf": "987654321",
        "endereco": "Rua B",
        "contas": [
            {"tipo": "corrente", "agencia": "0002", "num": 4321, "saldo": 1500.00}
        ]
    }
]

# Insira os documentos na coleção
collection.insert_many(clientes)


# Recuperar todos os clientes
todos_clientes = collection.find()
for cliente in todos_clientes:
    print(cliente)

# Recuperar cliente por CPF
cpf = "123456789"
cliente = collection.find_one({"cpf": cpf})
print(cliente)

# Recuperar contas de um cliente específico
nome_cliente = "Maria Oliveira"
cliente = collection.find_one({"nome": nome_cliente})
if cliente:
    contas = cliente.get("contas", [])
    for conta in contas:
        print(f'Tipo: {conta["tipo"]}, Agência: {conta["agencia"]}, Número: {conta["num"]}, Saldo: {conta["saldo"]}')
