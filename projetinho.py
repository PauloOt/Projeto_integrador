import mysql.connector



def cadastrar_carro():
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    ano = int(input("Digite o ano: "))

    sql = "INSERT INTO carros (marca, modelo, ano) VALUES (%s, %s, %s)"
    valores = (marca, modelo, ano)
    cursor.execute(sql, valores)
    db.commit()
    print("Carro cadastrado com sucesso!")


def listar_carros():
    cursor.execute("SELECT id, marca, modelo, ano FROM carros")
    resultados = cursor.fetchall()
    if resultados:
        print("\n=== Lista de Carros ===")
        for carro in resultados:
            print(f"ID: {carro[0]} | Marca: {carro[1]} | Modelo: {carro[2]} | Ano: {carro[3]}")
    else:
        print("Nenhum carro cadastrado.")


def deletar_carro():
    listar_carros()
    try:
        id_carro = int(input("\nDigite o ID do carro que deseja deletar: "))
        cursor.execute("DELETE FROM carros WHERE id = %s", (id_carro,))
        db.commit()
        if cursor.rowcount > 0:
            print("Carro deletado com sucesso!")
        else:
            print("Carro não encontrado.")
    except ValueError:
        print("ID inválido.")


def atualizar_carro():
    listar_carros()
    try:
        id_carro = int(input("\nDigite o ID do carro que deseja atualizar: "))
        cursor.execute("SELECT marca, modelo, ano FROM carros WHERE id = %s", (id_carro,))
        carro = cursor.fetchone()

        if not carro:
            print("Carro não encontrado.")
            return

        print("Digite os novos dados (pressione Enter para manter o valor atual):")
        nova_marca = input(f"Marca atual ({carro[0]}): ") or carro[0]
        novo_modelo = input(f"Modelo atual ({carro[1]}): ") or carro[1]
        novo_ano = input(f"Ano atual ({carro[2]}): ") or carro[2]

        sql = """
            UPDATE carros
            SET marca = %s, modelo = %s, ano = %s
            WHERE id = %s
        """
        valores = (nova_marca, novo_modelo, int(novo_ano), id_carro)
        cursor.execute(sql, valores)
        db.commit()
        print("Carro atualizado com sucesso!")

    except Exception as e:
        print("Erro ao atualizar:", e)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="070506", 
    database="sistema_carros"
)

cursor = db.cursor()


while True:
    print("\n=== MENU ===")
    print("1 - Cadastrar carro")
    print("2 - Atualizar carro")
    print("3 - Deletar carro")
    print("4 - Listar carros")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_carro()
    elif opcao == "2":
        atualizar_carro()
    elif opcao == "3":
        deletar_carro()
    elif opcao == "4":
        listar_carros()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
