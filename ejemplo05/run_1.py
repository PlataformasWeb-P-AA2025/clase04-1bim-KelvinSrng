import requests
import json

# Carga los datos desde el archivo JSON
with open('atp_tennis.json', 'r') as f:
    # Pasa los datos a estructuras de Python
    data = json.load(f)

base_datos = "personas005"
# Configura el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Enviar datos
response = requests.post(url, headers=headers, json=data)

# Mostrar respuesta
print(response.status_code)
print(response.json())