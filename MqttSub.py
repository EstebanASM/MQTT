import paho.mqtt.client as mqtt

# Configuración del broker MQTT
BROKER = "localhost"
PORT = 1883
TOPIC = "test/topic"

# Función de conexión
def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker con código {rc}")
    client.subscribe(TOPIC)

# Función de manejo de mensajes
def on_message(client, userdata, msg):
    print(f"Mensaje recibido: {msg.payload.decode()} en el tema {msg.topic}")

# Crear cliente MQTT
client = mqtt.Client()

# Asignar callbacks
client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker
client.connect(BROKER, PORT, 60)

# Mantener la conexión activa
client.loop_forever()
