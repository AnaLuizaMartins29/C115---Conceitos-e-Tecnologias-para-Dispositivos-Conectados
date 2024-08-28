class ChatbotEntregaComida:
    def __init__(self):
        self.rodando = True

    def iniciar_chat(self):
        print("Bem-vindo ao serviço de atendimento ao cliente da FoodExpress!")
        while self.rodando:
            self.mostrar_menu_principal()

    def mostrar_menu_principal(self):
        print("\nPor favor, escolha uma das seguintes opções:")
        print("1. Verificar status do pedido")
        print("2. Modificar pedido")
        print("3. Falar com um representante")
        print("4. Encerrar conexão")

        escolha = input("Digite a opção desejada: ")
        self.tratar_menu_principal(escolha)

    def tratar_menu_principal(self, escolha):
        if escolha == "1":
            self.verificar_status_pedido()
        elif escolha == "2":
            self.modificar_pedido()
        elif escolha == "3":
            self.falar_com_representante()
        elif escolha == "4":
            self.encerrar_conexao()
        else:
            print("Opção inválida. Tente novamente.")

    def verificar_status_pedido(self):
        numero_pedido = input("Por favor, insira o número do seu pedido: ")
        print(f"O status do seu pedido {numero_pedido} é: Em preparação.")
        self.mostrar_menu_principal()

    def modificar_pedido(self):
        print("Você pode modificar os seguintes itens do seu pedido:")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Voltar ao menu principal")

        escolha = input("Digite a opção desejada: ")
        if escolha == "1":
            item = input("Digite o nome do item que deseja adicionar: ")
            print(f"O item {item} foi adicionado ao seu pedido.")
        elif escolha == "2":
            item = input("Digite o nome do item que deseja remover: ")
            print(f"O item {item} foi removido do seu pedido.")
        elif escolha == "3":
            self.mostrar_menu_principal()
        else:
            print("Opção inválida. Tente novamente.")

        self.mostrar_menu_principal()

    def falar_com_representante(self):
        print("Aguarde enquanto conectamos você com um representante.")
        print("Representante conectado. Como posso ajudá-lo?")
        self.mostrar_menu_principal()

    def encerrar_conexao(self):
        print("Conexão encerrada. Obrigado por usar o FoodExpress!")
        self.rodando = False


if __name__ == "__main__":
    chatbot = ChatbotEntregaComida()
    chatbot.iniciar_chat()
