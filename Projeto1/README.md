#### Descrição do Projeto
Este projeto é um chatbot simples em Python que simula o atendimento ao cliente de uma empresa de entrega de comida. O chatbot permite ao cliente verificar o status do pedido, modificar o pedido ou falar com um representante.

#### Pré-requisitos
- Python 3.11 ou superior instalado no sistema.

#### Como Rodar o Chatbot
1. **Clone ou baixe o repositório**:
   - Clone o repositório ou faça o download dos arquivos necessários.

2. **Navegue até o diretório do projeto**:
   - Abra o terminal ou o prompt de comando.
   - Use o comando `cd` para navegar até o diretório onde o arquivo Python está localizado.

3. **Execute o script Python**:
   - No terminal, execute o seguinte comando:
     ```
     python nome_do_arquivo.py
     ```
     Substitua `nome_do_arquivo.py` pelo nome real do arquivo Python que contém o código.

4. **Interaja com o Chatbot**:
   - O chatbot irá iniciar e apresentará as opções disponíveis.
   - Siga as instruções fornecidas pelo chatbot para navegar pelo menu e executar as ações desejadas.

5. **Encerrar a Conexão**:
   - Para encerrar o chatbot, escolha a opção "4" no menu principal.

#### Estrutura do Código
- **ChatbotEntregaComida Class**: Esta classe contém todos os métodos necessários para o funcionamento do chatbot. Inclui métodos para iniciar o chat, exibir o menu principal, manipular as opções escolhidas pelo usuário, verificar o status do pedido, modificar o pedido, conectar com um representante e encerrar a conexão.
- **iniciar_chat()**: Método principal que inicia a interação com o usuário.
- **mostrar_menu_principal()**: Exibe as opções principais disponíveis.
- **tratar_menu_principal(escolha)**: Manipula a escolha do usuário no menu principal.
- **verificar_status_pedido()**: Simula a verificação do status de um pedido.
- **modificar_pedido()**: Permite ao usuário modificar itens no pedido.
- **falar_com_representante()**: Simula a conexão com um representante.
- **encerrar_conexao()**: Encerra a conexão e finaliza o chatbot.

