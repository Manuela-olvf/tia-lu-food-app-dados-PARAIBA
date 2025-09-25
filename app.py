# Parte 1: Cadastro e Consulta de Itens
itens = []
codigo_proximo_item = 1

def cadastrar_item():
    global codigo_proximo_item
    print("\nCadastrar novo item do cardápio")
    nome = input("Nome do item: ")
    descricao = input("Descrição: ")
    
    while True:
        try:
            preco = float(input("Preço: R$ "))
            break
        except ValueError:
            print("Digite um valor numérico válido para o preço.")
    
    while True:
        try:
            estoque = int(input("Quantidade em estoque: "))
            break
        except ValueError:
            print("Digite um número inteiro válido para o estoque.")
    
    item = (codigo_proximo_item, nome, descricao, preco, estoque)
    itens.append(item)
    codigo_proximo_item += 1
    print("Item cadastrado com sucesso!")

def consultar_itens():
    if not itens:
        print("Não há itens cadastrados.")
        return
    print("\n--- Cardápio ---")
    for i in itens:
        print(f"Código: {i[0]}, Nome: {i[1]}, Descrição: {i[2]}, Preço: R${i[3]}, Estoque: {i[4]}")

# Teste rápido
while True:
    print("\n1 - Cadastrar item\n2 - Consultar itens\n0 - Sair")
    escolha = input("Escolha: ")
    if escolha == "1":
        cadastrar_item()
    elif escolha == "2":
        consultar_itens()
    elif escolha == "0":
        break
    else:
        print("Opção inválida.")
