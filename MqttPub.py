import time
import paho.mqtt.client as mqtt

# Configuración del cliente MQTT
BROKER = "localhost"  # Cambia si Mosquitto está en otro servidor
PORT = 1883
TOPIC = "test/topic"

# Crear cliente
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

# Publicar mensajes periódicamente
try:
    while True:
        message = "Hola desde el publicador MQTT"
        client.publish(TOPIC, message)
        print(f"Publicando: {message}")
        time.sleep(2)  # Publicar cada 2 segundos
except KeyboardInterrupt:
    print("Publicador detenido")
