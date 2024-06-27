from conexao import conecta_db

def consultar(conexao):
    cursor = conexao.cursor()
    # Execução do Select no banco de dados
    cursor.execute(" select c.id, c.nome from cliente c ")
    # Recuperar os registros
    registros = cursor.fetchall()
    print("|---------------------------------------------------------|")
    print("|  ID   | NOME                                            |")        
    print("|---------------------------------------------------------|")
    for registro in registros:
        print(f"|  {registro[0]}  | {registro[1]}                    |")
    print("|---------------------------------------------------------|")


def inserir(conexao):
    cursor = conexao.cursor()
    nome_cliente   = str(input('Informe seu nome:'))

    sql_insert = "insert into cliente (nome) values ('"+ nome_cliente +  "')"
    cursor.execute(sql_insert)
   
    conexao.commit()


def alterar(conexao):
    cursor         = conexao.cursor()
    id             = int(input("Digite o ID:"))
    nome_cliente   = str(input('Informe seu nome:'))
  
    sql_update = "update cliente set nome = %s where id = %s"
    dados      = (nome_cliente,id)
    cursor.execute(sql_update, dados)
    conexao.commit()


def deletar(conexao):
    cursor     = conexao.cursor()
    id         = input("Digite o ID: ")

    sql_delete = "delete from cliente where id = " + id
    cursor.execute(sql_delete)
    conexao.commit()


def menu_cliente(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Cliente          |")
    print("|--------------------------------|")
    print("|     1 - Consultar cliente      |")
    print("|     2 - Inserir cliente        |")
    print("|     3 - Alterar cliente        |")
    print("|     4 - Deletar cliente        |")
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
