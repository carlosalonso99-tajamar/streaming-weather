from azure.eventhub import EventHubProducerClient
import os
from dotenv import load_dotenv
load_dotenv()
event_hub_conn_str = os.getenv('EVENT_HUB_CONNECTION_STRING')
event_hub_name = "weatherNamespaceCarlos"

try:
    print(f"Probando la conexión con la cadena: {event_hub_conn_str}")
    producer = EventHubProducerClient.from_connection_string(conn_str=event_hub_conn_str, eventhub_name=event_hub_name)
    print("Conexión establecida con éxito.")
except Exception as e:
    print(f"Error de autenticación o conexión: {str(e)}")
