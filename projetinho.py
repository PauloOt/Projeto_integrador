import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="070506",
    database="sistema_carros"
)

cursor = db.cursor()

def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
    db.commit()
    print("Cliente cadastrado.")

def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    for c in cursor.fetchall():
        print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]} | Telefone: {c[3]}")

def atualizar_cliente():
    listar_clientes()
    cliente_id = int(input("ID do cliente para atualizar: "))
    nome = input("Novo nome: ")
    email = input("Novo email: ")
    telefone = input("Novo telefone: ")
    cursor.execute("UPDATE clientes SET nome = %s, email = %s, telefone = %s WHERE id = %s",
                   (nome, email, telefone, cliente_id))
    db.commit()
    print("Cliente atualizado.")

def deletar_cliente():
    listar_clientes()
    cliente_id = int(input("ID do cliente para deletar: "))
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    db.commit()
    print("Cliente e seus carros deletados.")

def cadastrar_carro():
    listar_clientes()
    cliente_id = int(input("ID do cliente para o carro: "))
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cursor.execute("INSERT INTO carros (marca, modelo, ano, cliente_id) VALUES (%s, %s, %s, %s)",
                   (marca, modelo, ano, cliente_id))
    db.commit()
    print("Carro cadastrado.")

def listar_carros():
    cursor.execute("""
        SELECT carros.id, marca, modelo, ano, clientes.nome
        FROM carros
        JOIN clientes ON carros.cliente_id = clientes.id
    """)
    for c in cursor.fetchall():
        print(f"ID: {c[0]} | {c[1]} {c[2]} {c[3]} | Cliente: {c[4]}")

def atualizar_carro():
    listar_carros()
    carro_id = int(input("ID do carro para atualizar: "))
    marca = input("Nova marca: ")
    modelo = input("Novo modelo: ")
    ano = int(input("Novo ano: "))
    cursor.execute("UPDATE carros SET marca = %s, modelo = %s, ano = %s WHERE id = %s",
                   (marca, modelo, ano, carro_id))
    db.commit()
    print("Carro atualizado.")

def deletar_carro():
    listar_carros()
    carro_id = int(input("ID do carro para deletar: "))
    cursor.execute("DELETE FROM carros WHERE id = %s", (carro_id,))
    db.commit()
    print("Carro deletado.")


while True:
    print("\n=== MENU ===")

    print("=== CLIENTES ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Deletar cliente")

    print("\n=== CARROS ===")
    print("5 - Cadastrar carro")
    print("6 - Listar carros")
    print("7 - Atualizar carro")
    print("8 - Deletar carro")

    print("\n9 - Sair")

    op = input("\nOpção: ")

    if op == "1":
        cadastrar_cliente()
    elif op == "2":
        listar_clientes()
    elif op == "3":
        atualizar_cliente()
    elif op == "4":
        deletar_cliente()
    elif op == "5":
        cadastrar_carro()
    elif op == "6":
        listar_carros()
    elif op == "7":
        atualizar_carro()
    elif op == "8":
        deletar_carro()
    elif op == "9":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")

