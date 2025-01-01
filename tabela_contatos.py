import sqlite3

# Conecta ao banco de dados (ou cria se não existir)
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

# Cria a tabela de contatos (se não existir)
contact_table = """
    CREATE TABLE IF NOT EXISTS Contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
"""
cursor.execute(contact_table)

# Insere contatos iniciais
contatos = [
    {'nome': 'Alice', 'telefone': '1234567890', 'email': 'alice@example.com'},
    {'nome': 'Bob', 'telefone': '9876543210', 'email': 'bob@example.com'},
    {'nome': 'Charlie', 'telefone': '0987654321', 'email': 'charlie@example.com'}
]
cursor.executemany('INSERT INTO Contatos (nome, telefone, email) VALUES (?, ?, ?)', contatos)
conn.commit()

# Função para exibir todos os contatos
def exibir_contatos():
    cursor.execute("SELECT * FROM Contatos")  # Executa a consulta
    todos_contatos = cursor.fetchall()  # Recupera todos os resultados
    for contato in todos_contatos:
        print(contato)

# Função para buscar um contato pelo nome
def buscar_contato(nome):
    cursor.execute("SELECT * FROM Contatos WHERE nome=?", (nome,))
    contato_buscado = cursor.fetchone()
    if contato_buscado:
        print(contato_buscado)
    else:
        print("Contato não encontrado.")

# Função para atualizar um contato
def atualizar_contato():
    def atualizar(opcao, nome):
        if opcao == 1:
            telefone_atualizar = input("Digite o novo telefone: ")
            cursor.execute("UPDATE Contatos SET telefone=? WHERE nome=?", (telefone_atualizar, nome))
        else:
            email_atualizar = input("Digite o novo email: ")
            cursor.execute("UPDATE Contatos SET email=? WHERE nome=?", (email_atualizar, nome))
    opcao = int(input('1- Atualizar o telefone \n2- Atualizar o E-mail: '))
    nome_do_contato = input("Digite o nome do contato que deseja fazer a alteração: ")
    atualizar(opcao, nome_do_contato)
    conn.commit()

# Função para deletar um contato
def deletar_contato(nome_contato):
    cursor.execute("DELETE FROM Contatos WHERE nome=?", (nome_contato,))
    conn.commit()
    print("Contato excluído com sucesso.")

# Função principal do programa
def main():
    while True:
        print("\nMenu:")
        print("1- Exibir todos os contatos")
        print("2- Buscar um contato")
        print("3- Atualizar um contato")
        print("4- Deletar um contato")
        print("5- Sair")
        opcao_menu = int(input("Digite a opção desejada: "))

        if opcao_menu == 1:
            exibir_contatos()
        elif opcao_menu == 2:
            nome_buscar = input("Digite o nome do contato que deseja buscar: ")
            buscar_contato(nome_buscar)
        elif opcao_menu == 3:
            atualizar_contato()
        elif opcao_menu == 4:
            nome_excluir = input("Digite o nome do contato que deseja excluir: ")
            deletar_contato(nome_excluir)
        elif opcao_menu == 5:
            print("Programa encerrado.")
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
if __name__ == "__main__":
    main()