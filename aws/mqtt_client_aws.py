pip install paho-mqtt
import paho.mqtt.client as mqtt
import ssl

# Define the MQTT client
client = mqtt.Client()

# Configure TLS/SSL
client.tls_set(ca_certs="path/to/AmazonRootCA1.pem",
               certfile="path/to/certificate.pem.crt",
               keyfile="path/to/private.pem.key",
               tls_version=ssl.PROTOCOL_TLSv1_2)

# Define the callback for when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Set the on_message callback
client.on_message = on_message

# Connect to the AWS IoT Core endpoint
client.connect("your-iot-endpoint.amazonaws.com", 8883)

# Subscribe to the desired topic
client.subscribe("your/topic")

# Start the MQTT client loop
client.loop_start()