# EJERCICIO 1
import json
import requests
from random import randint

def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic

def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data

def altura(item):
    # print(item, type(item))
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return -1

def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return -1


id1 = randint(1, 83)
personaje1 = get_charter_by_id(id1)

id2 = randint(1, 83)
personaje2 = get_charter_by_id(id2)

if(altura(personaje1) > altura(personaje2)):
   print("El personaje mas alto es",personaje1["name"],"la altura es", altura(personaje1))
else:
    print("El personaje mas alto es",personaje2["name"],"la altura es", altura(personaje2))

if(peso(personaje1)) > (peso(personaje2)):
   print("El personaje mas pesado es",personaje1["name"],"el peso es", altura(personaje1))
else:
    print("El personaje mas pesado es",personaje2["name"],"el peso es", altura(personaje2))


if(personaje1 == "Yoda" or personaje2 == "Grievous" or  personaje1 == "Grievous" or personaje2 == "Yoda"):
    print(personaje1)
    print(personaje2)





