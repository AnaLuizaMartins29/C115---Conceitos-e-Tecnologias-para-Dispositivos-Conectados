from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import paho.mqtt.client as mqtt

class WindowControlApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Widget de imagem para representar o estado da janela
        self.window_image = Image(source='closed.jpg')  # Estado inicial: janela fechada
        self.layout.add_widget(self.window_image)

        # Botão para abrir a janela
        self.button_toggle = Button(text='Abrir Janela')
        self.button_toggle.bind(on_press=self.toggle_window)
        self.layout.add_widget(self.button_toggle)

        # Configurar o cliente MQTT
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        self.client.connect("mqtt.eclipseprojects.io", 1883, 60)

        # Estado inicial da janela
        self.is_open = False

        return self.layout

    def toggle_window(self, instance):
        if self.is_open:
            self.send_mqtt_command("fechar")  # Comando para fechar a janela
            self.is_open = False
        else:
            self.send_mqtt_command("abrir")  # Comando para abrir a janela
            self.is_open = True

    def send_mqtt_command(self, command):
        topic = "window/control"  # Novo tópico para controle da janela
        self.client.publish(topic, command)

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado com código de resultado: " + str(rc))

    def on_publish(self, client, userdata, mid):
        # Atualizar a imagem e o botão com base no estado da janela
        if self.is_open:
            print("Abrindo janela...")
            self.window_image.source = 'open.jpg'
            self.button_toggle.text = 'Fechar Janela'
        else:
            print("Fechando janela...")
            self.window_image.source = 'closed.jpg'
            self.button_toggle.text = 'Abrir Janela'

if __name__ == '__main__':
    WindowControlApp().run()