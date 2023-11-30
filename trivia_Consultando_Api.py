import json
import requests

numero = input("Ingrese un número: ")
response = requests.get(f"http://numbersapi.com/{numero}?json")
trivia = json.loads(response.content)
print(trivia)
