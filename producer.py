from azure.eventhub import EventHubProducerClient, EventData
import os
import json
from dotenv import load_dotenv
load_dotenv()

# Obtener la cadena de conexión del Event Hub
event_hub_conn_str = os.getenv('EVENT_HUB_CONNECTION_STRING')
event_hub_name = "weather-data"

# Imprimir la cadena de conexión y el nombre del Event Hub para verificar
print("Cadena de conexión del Event Hub:", event_hub_conn_str)
print("Nombre del Event Hub:", event_hub_name)

# Crear el productor del Event Hub
try:
    print("Creando el productor del Event Hub...")
    producer = EventHubProducerClient.from_connection_string(conn_str=event_hub_conn_str, eventhub_name=event_hub_name)
    print("Productor del Event Hub creado exitosamente.")
    
    with producer:
        print("Preparando el mensaje de prueba para enviar...")
        test_data = {"test": "Este es un mensaje de prueba"}
        event_data = EventData(json.dumps(test_data))
        
        # Enviar el mensaje al Event Hub
        print("Enviando el mensaje al Event Hub...")
        producer.send_batch([event_data])
        print("Mensaje de prueba enviado correctamente al Event Hub.")
except Exception as e:
    print(f"Error al enviar el mensaje de prueba: {str(e)}")
