import json
import csv

# Se lee el archivo CSV
with open('atp_tennis.csv', mode='r', encoding='ISO-8859-1') as archivo_csv:
	
	# Transforma el CSV en una lista de diccionarios
	lectura_csv = csv.DictReader(archivo_csv)
	# Crea una lista de diccionarios
	lista = []
	for r in lectura_csv:
		lista.append(r)

# Diccionario final para transformar a JSON
diccionario = {"docs": lista}

# Guarda/Escribi en un archivo JSON
with open('atp_tennis.json', mode='w', encoding='utf-8') as archivo_json:
	json.dump(diccionario, archivo_json, indent=4)

print('Script finalizado.')