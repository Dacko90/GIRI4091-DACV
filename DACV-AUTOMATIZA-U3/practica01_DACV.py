import requests
import json

def GetAllProducts():
    url = 'https://fakestoreapi.com/products'
    Respuesta = requests.get(url).json()
    print("Listado de productos")
    print('-------------------------')
    print(json.dumps(Respuesta, indent=4, ensure_ascii=False))


def GetProduct():
    id_product = input('ID del producto: \n')
    url='https://fakestoreapi.com/products/' + id_product
    Respuesta = requests.get(url).json()
    print("Búsqueda de producto")
    print(json.dumps(Respuesta, indent=4, ensure_ascii=False))

    
def AddProduct():
    product_id = int(input("Ingrese el ID del producto: "))
    title = input("Ingrese el título del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    description = input("Ingrese la descripción del producto: ")
    category = input("Ingrese la categoría del producto: ")
    image = input("Ingrese la URL de la imagen del producto: ")
    rating_rate = float(input("Ingrese la calificación del producto: "))
    rating_count = int(input("Ingrese el número de calificaciones del producto: "))

    datos = {
        "id": product_id,
        "title": title,
        "price": price,
        "description": description,
        "category": category,
        "image": image,
        "rating": {
            "rate": rating_rate,
            "count": rating_count
        }
    }
    
    url = 'https://fakestoreapi.com/products'
    
    try:
        response = requests.post(url, json=datos, headers={'Content-Type': 'application/json'})
        response.raise_for_status() 
        added_product = response.json()
        print("Producto agregado exitosamente:", added_product)
    except requests.exceptions.RequestException as e:
        print("Error al agregar el producto:", e)
        if response is not None:
            print("Respuesta del servidor:", response.text)

def UpdateProduct():
    product_id = input("Ingrese el ID del producto a modificar: ")
    url = 'https://fakestoreapi.com/products/' + product_id
    
    title = input("Ingrese el nuevo título del producto (o presione Enter para omitir): ")
    price = input("Ingrese el nuevo precio del producto (o presione Enter para omitir): ")
    description = input("Ingrese la nueva descripción del producto (o presione Enter para omitir): ")
    category = input("Ingrese la nueva categoría del producto (o presione Enter para omitir): ")
    image = input("Ingrese la nueva URL de la imagen del producto (o presione Enter para omitir): ")
    rating_rate = input("Ingrese la nueva calificación del producto (o presione Enter para omitir): ")
    rating_count = input("Ingrese el nuevo número de calificaciones del producto (o presione Enter para omitir): ")

    datos = {}
    if title:
        datos['title'] = title
    if price:
        datos['price'] = float(price)
    if description:
        datos['description'] = description
    if category:
        datos['category'] = category
    if image:
        datos['image'] = image
    if rating_rate:
        if 'rating' not in datos:
            datos['rating'] = {}
        datos['rating']['rate'] = float(rating_rate)
    if rating_count:
        if 'rating' not in datos:
            datos['rating'] = {}
        datos['rating']['count'] = int(rating_count)
    
    try:
        response = requests.put(url, json=datos, headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        updated_product = response.json()
        print("Producto modificado exitosamente:", updated_product)
    except requests.exceptions.RequestException as e:
        print("Error al modificar el producto:", e)
        if response is not None:
            print("Respuesta del servidor:", response.text)


def DeleteProduct():
    product_id = input("Ingrese el ID del producto a eliminar: ")
    url = 'https://fakestoreapi.com/products/' + product_id
    
    try:
        response = requests.delete(url, headers={'Content-Type': 'application/json'})
        response.raise_for_status()
        print("Producto eliminado exitosamente.")
    except requests.exceptions.RequestException as e:
        print("Error al eliminar el producto:", e)
        if response is not None:
            print("Respuesta del servidor:", response.text)


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