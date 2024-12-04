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

Autor
Nome: Ana Luiza Martins
Matrícula: 1701
