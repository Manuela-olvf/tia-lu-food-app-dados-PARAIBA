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
# Parte 2: Atualizar Itens
def atualizar_item():
    if not itens:
        print("Não há itens cadastrados.")
        return
    
    print("\nItens disponíveis:")
    for i in itens:
        print(f"Código: {i[0]}, Nome: {i[1]}, Preço: R${i[3]}, Estoque: {i[4]}")
    
    try:
        codigo = int(input("Digite o código do item que deseja atualizar: "))
    except ValueError:
        print("Código inválido.")
        return
    
    encontrado = False
    for index in range(len(itens)):
        if itens[index][0] == codigo:
            encontrado = True
            print(f"Atualizando item: {itens[index][1]}")
            
            novo_nome = input("Novo nome (pressione enter para manter): ")
            nova_descricao = input("Nova descrição (pressione enter para manter): ")
            
            while True:
                preco_input = input("Novo preço (pressione enter para manter): ")
                if preco_input == "":
                    novo_preco = itens[index][3]
                    break
                try:
                    novo_preco = float(preco_input)
                    break
                except ValueError:
                    print("Digite um valor válido.")
            
            while True:
                estoque_input = input("Novo estoque (pressione enter para manter): ")
                if estoque_input == "":
                    novo_estoque = itens[index][4]
                    break
                try:
                    novo_estoque = int(estoque_input)
                    break
                except ValueError:
                    print("Digite um número inteiro válido.")
            
            itens[index] = (
                itens[index][0],
                novo_nome if novo_nome else itens[index][1],
                nova_descricao if nova_descricao else itens[index][2],
                novo_preco,
                novo_estoque
            )
            print("Item atualizado com sucesso!")
            break
    
    if not encontrado:
        print("Item não encontrado.")

# Parte 3: Criar Pedidos e Fila de Pedidos Pendentes
fila_pedidos_pendentes = []
codigo_proximo_pedido = 1

def criar_pedido():
    global codigo_proximo_pedido
    if not itens:
        print("Não há itens no cardápio para criar pedido.")
        return
    
    pedido_itens = []
    while True:
        print("\nItens disponíveis:")
        for i in itens:
            print(f"Código: {i[0]}, Nome: {i[1]}, Preço: R${i[3]}, Estoque: {i[4]}")
        
        try:
            codigo_item = int(input("Digite o código do item que deseja adicionar: "))
        except ValueError:
            print("Código inválido.")
            continue
        
        encontrado = False
        for item in itens:
            if item[0] == codigo_item:
                encontrado = True
                if item[4] == 0:
                    print("Item sem estoque.")
                    break
                pedido_itens.append(item)
                print(f"Item '{item[1]}' adicionado ao pedido.")
                break
        
        if not encontrado:
            print("Item não encontrado.")
        
        mais = input("Deseja adicionar outro item? (s/n): ").lower()
        if mais != 's':
            break
    
    if not pedido_itens:
        print("Nenhum item selecionado. Pedido cancelado.")
        return
    
    total = sum(item[3] for item in pedido_itens)
    cupom = input("Deseja aplicar cupom de desconto (%)? Caso não, pressione enter: ")
    if cupom:
        try:
            desconto = float(cupom)
            total = total * (1 - desconto / 100)
        except ValueError:
            print("Cupom inválido. Nenhum desconto aplicado.")
    
    pedido = (codigo_proximo_pedido, pedido_itens, total, "AGUARDANDO APROVACAO")
    fila_pedidos_pendentes.append(pedido)
    print(f"\nPedido {codigo_proximo_pedido} criado com sucesso! Total: R${total:.2f}")
    codigo_proximo_pedido += 1
    
