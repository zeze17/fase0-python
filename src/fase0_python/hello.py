# Un programa simple de Python que saluda y usa una librería externa (como 'requests')
import requests


def saludar_con_estilo():
    respuesta = requests.get("https://api.chucknorris.io/jokes/random")
    datos = respuesta.json()

    print("¡Hola! Aquí tienes una frase aleatoria:")
    print(datos["value"])


def hello_there(name: str) -> str:
    return (f"hello, {name}")

def hello_there_last(name: str, lastname: str) :
    print(f"hello, your name is {name} and last name is {lastname}")

def hello_there_example(name: str) -> str:
    return (f"hello, {name} and the numer of leter is {len(name)}")

if __name__ == "__main__":
    saludar_con_estilo()
    resultado = hello_there("Alice")
    print(resultado)
    resultado_example = hello_there_example("Alice")
    print(resultado_example)
    hello_there_last("Bob", "robert")