#EJERCICIO 2
import json
import requests
import random

def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic

def get_charter_by_id(id):
    respuesta = requests.get('https://swapi.dev/api/people/'+str(id))
    if respuesta.status_code == 200:
        dic = json.loads(respuesta.text)
        return dic


def get_random_character():
    randomCharacterId = random.randrange(1, 82, 2)
    character = get_charter_by_id(randomCharacterId)
    return character

def main():
    personaje1 = get_random_character()
    personaje2 = get_random_character()
    beenInMoreMovies = personaje1 if len(personaje1['films']) > len(personaje2['films']) else personaje2
    print('El que estuvo en mas peliculas es: ' + str(beenInMoreMovies.get('name')))
        
main()