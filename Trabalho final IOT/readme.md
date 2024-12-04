# Sistema IoT de Controle de Janelas

Este projeto implementa um sistema IoT para controle remoto de janelas usando a biblioteca Kivy para a interface gráfica e MQTT para a comunicação entre o dispositivo e o servidor. O sistema permite ao usuário abrir ou fechar janelas de maneira remota através de um aplicativo simples.

## Funcionalidade

O sistema de controle de janelas funciona da seguinte forma:
- O usuário interage com um botão na interface gráfica para enviar comandos de controle (ex: abrir ou fechar a janela).
- Quando o botão é pressionado, uma mensagem é publicada em um broker MQTT.
- A imagem na interface gráfica é atualizada para refletir o estado da janela (aberta ou fechada).

## Tecnologias Utilizadas

- **Kivy**: Framework para criação de interfaces gráficas.
- **MQTT**: Protocolo de comunicação para dispositivos IoT.
- **Python**: Linguagem de programação utilizada para o desenvolvimento.

## Estrutura do Projeto



## Instalação

### 1. Instalar as dependências

Este projeto requer a instalação de algumas bibliotecas Python. Crie um ambiente virtual (opcional, mas recomendado) e instale as dependências com o seguinte comando:

```bash
pip install kivy paho-mqtt

## Kivy: Usado para criar a interface gráfica.
## paho-mqtt: Cliente MQTT para comunicação com o servidor/broker.

### 2. Baixar as imagens
Este código depende de duas imagens (closed.jpg e open.jpg) que representam o estado da janela (fechada e aberta, respectivamente). Certifique-se de ter essas imagens na mesma pasta onde o código está.

### 3. Rodando o código

Para rodar o código, basta executar o arquivo main.py:

```bash
python main.py

Isso abrirá a interface gráfica do Kivy com um botão "Abrir Janela". Quando o botão for pressionado, o sistema enviará um comando MQTT para o dispositivo controlado (que pode ser um motor ou atuador) para abrir ou fechar a janela. 
A imagem na interface gráfica será atualizada conforme o estado da janela.

### 4. Testando a Conexão MQTT
O código está configurado para usar um broker MQTT público (mqtt.eclipseprojects.io), mas você pode configurar um broker privado se necessário.



Autor
Nome: [Ana Luiza Martins]
Matrícula: [1701]


