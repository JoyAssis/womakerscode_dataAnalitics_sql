import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conection = sqlite3.connect('banco')
cursor = conection.cursor()

# 1. Criar a tabela alunos
# cursor.execute('''
# CREATE TABLE alunos (
#     id INT,
#     nome TEXT,
#     idade INT,
#     curso TEXT
# )
# ''')

#2. Insira pelo menos 5 registros
# cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(1, 'João', 20, 'Engenharia')")
# cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(2, 'Lívia', 22, 'Direito')")
# cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(3, 'Gustavo', 21, 'Medicina')")
# cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(4, 'Ana Clara', 19, 'Engenharia')")
# cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES(5, 'Luiz', 23, 'Letras')")

#3. Consultas básicas
# a) Selecione todos os registros da talela alunos
# alunos = cursor.execute('SELECT * FROM alunos')
# for aluno in alunos:
#     print(aluno)

# b) Selecione o nome e a idade dos alunos com mais de 20 anos
# alunos_idade = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# for aluno in alunos_idade:
#     print(aluno)

# c) Selecione os alunos do curso de "Engenharia" em ordem alfabética
#a_z_order = cursor.execute("SELECT nome FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")
#for aluno in a_z_order:
#    print(aluno)

# d) Contar o número total de alunos na tabela
#cursor.execute("SELECT COUNT(*) FROM alunos")
#numero_total_alunos = cursor.fetchall()[0]
#print(f"Total de alunos {numero_total_alunos}")


#4. Atualizações e remoções
# a) Atualize a idade de um alunos específico na tabela
#cursor.execute("UPDATE alunos SET curso  = 'Pedagogia' WHERE id = 2")
# b) Remova um aluno da tabela pelo id
#cursor.execute("DELETE FROM alunos WHERE id = 5")

#5. Criar uma tabela e Inserir dados
# Crie uma tabela chamada "clientes" com os campos: id(chave primária), nome(texto), idade(inteiro) e saldo(float). Insira alguns registros nessa tabela.
# cursor.execute('''
# CREATE TABLE clientes(
#     id INT PRIMARY KEY,
#     nome VARCHAR(10),
#     idade INT,
#     saldo FLOAT 
# )
# ''')
# dados_clientes = [
#     (1, 'Izabela', 27, 121.75),
#     (2, 'Carlos', 35, 250.00),
#     (3, 'Mariana', 22, 89.50),
#     (4, 'Fernanda', 40, 375.30),
#     (5, 'Fatima', 60, 800),
#     (6, 'Carol', 35, 25.00),
#     (7, 'Maria', 22, 79),
#     (8, 'Fernando', 55, 375)
# ]
# cursor.executemany("INSERT INTO clientes (id, nome, idade, saldo) VALUES(?,?,?,?)", dados_clientes)



#6. Consultas agregadas
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
# idade_maior = cursor.execute("SELECT nome,idade FROM clientes WHERE idade > 30")
# for cliente in idade_maior:
#     print(cliente)

# b) Calcule o saldo médio dos clientes
# cursor.execute("SELECT AVG(saldo) FROM clientes")
# saldo_medio = cursor.fetchone()[0]
# print(f"Saldo médio dos clientes: {saldo_medio}")

# c) Encontre o cliente com saldo máximo
# cursor.execute("SELECT nome, MAX(saldo) FROM clientes")
# saldo_max = cursor.fetchone()
#print(f"Cliente com saldo máximo: {saldo_max}")

# d) Conte quantos clientes tem saldo acima de 1000
#cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
#clientes_saldo = cursor.fetchone()[0]
#print(f"Clientes com saldo acima de 1000: {clientes_saldo}")

 #7. Atualizações e remoções com condições
# a) Atualize o saldo de um cliente específico
#cursor.execute("UPDATE clientes SET saldo = 200 WHERE id = 2")
#for cliente in cursor.execute("SELECT * FROM clientes"):
#    print(cliente)

# b) Remova um cliente da tabela pelo id
#cursor.execute("DELETE FROM clientes WHERE id = 3")
# for cliente in cursor.execute("SELECT * FROM clientes"):
#     print(cliente)

 #8. Junção de tabelas
# Crie uma tabela chamada "compras" com os campos: id(chave primária), cliente_id(chave estrangeira referenciando o id da tabela clientes), produto(texto) e valor(real). Insira algumas compras associadas a clientes existentes na tabela clientes. Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
cursor.execute('''
CREATE TABLE compras(
    id INT PRIMARY KEY,
    cliente_id INT,
    produto VARCHAR(20),
    valor REAL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
''')

dados_compras = [
    (1, 1, 'Notebook', 4500.00),
    (2, 2, 'Smartphone', 2500.00),
    (3, 4, 'Teclado', 300.00),
    (4, 5, 'Monitor', 1200.00),
    (5, 7, 'Mochila', 150.00),
    (6, 8, 'Headset', 350.00)
]

cursor.executemany("INSERT INTO compras (id, cliente_id, produto, valor) VALUES (?, ?, ?, ?)", dados_compras)

# Confirmar e verificar os dados inseridos
cursor.execute("SELECT * FROM compras")
compras_resultados = cursor.fetchall()


# cursor.execute('''
#     SELECT clientes.nome, compras.produto, compras.valor 
#     FROM compras
#     JOIN clientes ON compras.cliente_id = clientes.id
# ''')

# compras_resultados = cursor.fetchall()

# print("\nCompras realizadas:")
# for compra in compras_resultados:
#     print(f"Cliente: {compra[0]}, Produto: {compra[1]}, Valor: {compra[2]:.2f}")

# Confirmar as mudanças e fechar a conexão
conection.commit()
conection.close()