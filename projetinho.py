import mysql.connector

db = mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="sistema_carros"
)

cursor = db.cursor()


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
    db.commit()
    print("\033[1;32mCliente cadastrado.\033[m")

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
    print("\033[1;32mCliente atualizado.\033[m")

def deletar_cliente():
    listar_clientes()
    cliente_id = int(input("ID do cliente para deletar: "))
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    db.commit()
    print("\033[1;32mCliente e seus carros deletados.\033[m")


def cadastrar_carro():
    listar_clientes()
    cliente_id = int(input("ID do cliente para o carro: "))
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cursor.execute("INSERT INTO carros (marca, modelo, ano, cliente_id) VALUES (%s, %s, %s, %s)",
                   (marca, modelo, ano, cliente_id))
    db.commit()
    print("\033[1;32mCarro cadastrado.\033[m")

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
    print("\033[1;32mCarro atualizado.\033[m")

def deletar_carro():
    listar_carros()
    carro_id = int(input("ID do carro para deletar: "))
    cursor.execute("DELETE FROM carros WHERE id = %s", (carro_id,))
    db.commit()
    print("\033[1;93mCarro deletado.\033[m")


def menu_clientes():
    while True:
        print("\033[1;93m=== MENU CLIENTES ===\033[m")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Deletar cliente")
        print("5 - Voltar")

        op = input("Opção: ")
        if op == "1":
            cadastrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            atualizar_cliente()
        elif op == "4":
            deletar_cliente()
        elif op == "5":
            break
        else:
            print("\033[1;31mOpção inválida.\033[m")

def menu_carros():
    while True:
        print("\n\033[1;93m=== MENU CARROS ===\033[m")
        print("1 - Cadastrar carro")
        print("2 - Listar carros")
        print("3 - Atualizar carro")
        print("4 - Deletar carro")
        print("5 - Voltar")

        op = input("Opção: ")
        if op == "1":
            cadastrar_carro()
        elif op == "2":
            listar_carros()
        elif op == "3":
            atualizar_carro()
        elif op == "4":
            deletar_carro()
        elif op == "5":
            break
        else:
            print("\033[1;31mOpção inválida.\033[m")


while True:
    print("\n\033[1;93m=== MENU PRINCIPAL ===\033[m")
    print("1 - Gerenciar Clientes")
    print("2 - Gerenciar Carros")
    print("3 - Sair")

    op = input("Opção: ")
    if op == "1":
        menu_clientes()
    elif op == "2":
        menu_carros()
    elif op == "3":
        print("Saindo...")
        break
    else:
        print("\033[1;31mOpção inválida.\033[m")
        