import requests
import json

def GetAllProducts():
    url = 'https://fakestoreapi.com/products'
    Respuesta = requests.get(url).json()
    print("Listado de productos")
    print('-------------------------')
    print(json.dumps(Respuesta, indent=4, ensure_ascii=False))


def GetProduct():
    print("Búsqueda de producto")
    
def AddProduct():
    print("Agregar producto")


def UpdateProduct():
    print("Modificar producto")


def DeleteProduct():
    print("Eliminación de producto")


def mostrar_menu():
    print("\nAdministración de Productos:")
    print("1. Consultar todos los productos")
    print("2. Consultar un producto en específico")
    print("3. Agregar un nuevo producto")
    print("4. Modificar producto en específico")
    print("5. Eliminar un producto")
    print("6. Salir")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == '1':
        GetAllProducts()
    elif opcion == '2':
        GetProduct()
    elif opcion == '3':
        AddProduct()
    elif opcion == '4':
        UpdateProduct()    
    elif opcion == '5':
        DeleteProduct()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intenta de nuevo.")