import requests
import os

url = input("Wpisz url: ")
filename = input("Wpisz nazwę pliku: ")

response = requests.get(url)

if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
        print("Wideo zostało pobrane!")
else:
    print("Nie udało się pobrać wideo.")