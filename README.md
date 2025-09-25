# 🍔 Sistema de Gerenciamento de Pedidos

## 👥 Equipe
- Membro 1: MANUELA FIGUEIRA
- Membro 2: LORENA DIAS    
- Membro 3: RAFAELA CANGUÇU
- Membro 4: SAMUEL NASCIMENTO
- Membro 5: JOICE ROCHA

---

## 📖 Descrição
Este projeto é um **sistema de gerenciamento de pedidos** desenvolvido em Python.  
O objetivo é simular o funcionamento básico de um restaurante utilizando **estruturas de dados nativas** para representar filas de pedidos e operações de gerenciamento de itens e pedidos.

O sistema é operado por meio de um **menu interativo em linha de comando**, oferecendo funcionalidades para manipulação do **menu de itens** e do **fluxo de pedidos**.

---

## ⚙️ Estrutura e Funcionalidades

### 🔹 Gerenciar Menu de Itens
- **Cadastrar Item**: Adiciona um novo produto ao menu.  
- **Atualizar Item**: Modifica informações de um item existente (nome, descrição, preço, quantidade em estoque).  
- **Consultar Itens**: Exibe todos os itens disponíveis.  

Cada item é armazenado com as seguintes informações:
- `código`: Identificador único (gerado automaticamente).
- `nome`: Nome do produto.
- `descrição`: Detalhes sobre o item.
- `preço`: Valor monetário.
- `estoque`: Quantidade em estoque.

---

### 🔹 Gerenciar Menu de Pedidos
- **Criar Pedido**:  
  - Deve conter no mínimo **um item**.  
  - Pode ter um **cupom de desconto** aplicado.  
  - Ao ser criado, o pedido é considerado **pago** e recebe o status inicial `AGUARDANDO APROVACAO`.  

- **Processar Pedidos Pendentes**:  
  - Permite **aceitar ou rejeitar** pedidos na ordem em que foram criados.  

- **Atualizar Status de Pedido**:  
  - Altera o status de um pedido existente de acordo com o fluxo definido.  

- **Cancelar Pedido**:  
  - Só é possível se o status for `AGUARDANDO APROVACAO` ou `ACEITO`.

---

### 🔹 Fluxo de Pedidos e Filas
O sistema usa **filas (FIFO)** para gerenciar os pedidos:

1. **Fila de Pedidos Pendentes**  
   - Todos os novos pedidos são adicionados aqui.  
   - Processados na ordem de chegada.  

2. **Fila de Pedidos Aceitos**  
   - Pedidos aceitos são movidos para cá com status `FAZENDO`.  

3. **Fila de Pedidos Prontos**  
   - Após o preparo, recebem status `FEITO` e ficam aguardando entregador (`ESPERANDO ENTREGADOR`).  

---

### 🔹 Fluxo de Status do Pedido
Os pedidos podem assumir os seguintes status:

- `AGUARDANDO APROVACAO`
- `ACEITO`
- `FAZENDO`
- `FEITO`
- `ESPERANDO ENTREGADOR`
- `SAIU PARA ENTREGA`
- `ENTREGUE`
- `CANCELADO`
- `REJEITADO`

---

### 🔹 Consultas
O sistema permite:
- Exibir **todos os pedidos**.  
- Filtrar pedidos por **status**.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**  
- Estruturas de dados nativas (`list`, `queue`)  
- Menu interativo no terminal  

---

## ▶️ Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   cd repositorio
