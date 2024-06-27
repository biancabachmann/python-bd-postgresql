from conexao import conecta_db


def consultar(conexao):
    cursor = conexao.cursor()
    # Execução do Select no banco de dados
    cursor.execute(" select p.id, p.descricao, p.preco, p.estoque, categoria.nome from produto p " + 
                   " inner join categoria on (p.categoria_id = categoria.id)")
    # Recuperar os registros
    registros = cursor.fetchall()
    print("|---------------------------------------------------------|")
    print("|  ID   | Descrição       |Preço | Estoque   | Categoria  |")        
    print("|---------------------------------------------------------|")
    for registro in registros:
        print(f"|  {registro[0]}  | {registro[1]}  | {registro[2]} | {registro[3]}  | {registro[4]}")
    print("|---------------------------------------------------------|")


def inserir(conexao):
    cursor = conexao.cursor()
    descricao     = input('Digite a descricao do produto: ')
    preco         = float(input('Digite o preço do produto: '))
    estoque       = float(input('Digite o estoque do produto: '))
    categoria_id  = int(input('Digite o ID da categoria: '))
    

    sql_insert = "insert into produto (descricao, preco, estoque, categoria_id) values (%s, %s, %s, %s)"
    dados      = (descricao, preco, estoque, categoria_id)
    cursor.execute(sql_insert, dados)
    conexao.commit()

def alterar(conexao):
    cursor     = conexao.cursor()
    id         = input("Digite o ID: ")
    descricao  = input('Digite a descrição: ')
    preco      = float (input('Digite o preço: '))
    estoque    = float (input('Digite a quantidade de estoque: '))
    categoria_id  = int(input('Digite o ID da categoria: '))
    

    sql_update = "update produto set descricao = %s, preco = %s, estoque = %s, categoria_id %s where id = %s"
    dados      = (descricao, preco, estoque, categoria_id,id)
    cursor.execute(sql_update, dados)
    conexao.commit()

def deletar(conexao):
    cursor     = conexao.cursor()
    id         = input("Digite o ID: ")

    sql_delete = "delete from produto where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()


def menu_produto(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Produto          |")
    print("|--------------------------------|")
    print("|     1 - Consultar Produto      |")
    print("|     2 - Inserir Produto        |")
    print("|     3 - Alterar Produto        |")
    print("|     4 - Deletar Produto        |")
    print("|     5 - Sair do Sistema        |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            consultar(conexao)
        elif opcao == "2":
            inserir(conexao)
        elif opcao == "3":
            alterar(conexao)
        elif opcao == "4":
            deletar(conexao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")