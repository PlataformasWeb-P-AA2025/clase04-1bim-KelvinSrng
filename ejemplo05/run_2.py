import requests
import json

# Carga los datos desde el archivo JSON
with open('atp_tennis.json', 'r') as f:
    # Pasa los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    lista_datos.append(d)

base_datos = "personas006"
# Configura el acceso a la base de datos
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Se procede a enviar los datos
for doc in lista_datos:
    response = requests.post(url, json=doc)
    print(f"Insertando partido {doc['Player_1']} vs {doc['Player_2']} | {response.status_code}")
