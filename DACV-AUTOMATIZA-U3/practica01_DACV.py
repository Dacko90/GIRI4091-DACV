import requests
import json

def GetAllProducts():
    url = "https://fakestoreapi.com/products"
    respuesta = requests.get(url).json()
    print("Listado de productos")
    print("---------------------")
    print(json.dumps(respuesta, indent=4, ensure_ascii=False))

def GetProduct():
    try:
        id = input("Ingresa el ID del producto: ")
        url = "https://fakestoreapi.com/products/" + id
        response = requests.get(url)
        
        if response.status_code == 404:
            print("El producto no existe. Por favor, verifica el ID e intenta nuevamente.")
        else:
            response.raise_for_status()  
            producto = response.json()
            if not producto:
                print("El producto no existe o no se encontró el producto.")
            else:
                print("Búsqueda de producto")
                print("---------------------")
                print(json.dumps(producto, indent=4, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print("Error al buscar el producto:", e)
    except Exception as e:
        print("Ha ocurrido un error:", e)

def AddProduct():
    print("\nAgregar producto\n")
    url = "https://fakestoreapi.com/products"
    titleProduct = input("Ingresa el título del producto:\n")
    priceProduct = input("Ingresa el precio del producto:\n")
    descriptionProduct = input("Ingresa la descripción del producto:\n")
    categoryProduct = input("Ingresa la categoría del producto:\n")

    payload = {
        "title": titleProduct,
        "price": priceProduct,
        "description": descriptionProduct,
        "category": categoryProduct,
        "image": "https://fakestoreapi.com/img/placeholder.jpg",
        "rating": {
            "rate": 4.5,
            "count": 10
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("\nProducto creado exitosamente")
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    else:
        print("\nError al crear el producto")
        print("Código de estado:", response.status_code)
        print("Respuesta del servidor:", response.text)

def DeleteProduct():
    try:
        id = input("Ingresa el ID del producto a eliminar: ")
        url = "https://fakestoreapi.com/products/" + id
        response = requests.delete(url)

        if response.status_code == 404:
            print("Producto no encontrado. Por favor, verifica el ID e intenta nuevamente.")
        else:
            response.raise_for_status()  
            respuesta_json = response.json()
            if respuesta_json is None or "error" in respuesta_json or not respuesta_json:
                print("El producto no existe o no se encontró. No se realizó ninguna eliminación.")
            else:
                print("Producto eliminado exitosamente.")
                print(json.dumps(respuesta_json, indent=4, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
    except Exception as e:
        print("Ha ocurrido un error:", e)

def UpdateProduct():
    try:
        id = input("Ingresa el ID del producto a modificar: ")
        url = "https://fakestoreapi.com/products/" + id
        data = {
            "title": input("Nuevo título: "),
            "price": float(input("Nuevo precio: ")),
            "description": input("Nueva descripción: "),
            "category": input("Nueva categoría: "),
            "image": "https://fakestoreapi.com/img/placeholder.jpg",
        }

        response = requests.put(url, json=data)
        if response.status_code == 404:
            print("El producto no existe. Por favor, verifica el ID e intenta nuevamente.")
            return
        response.raise_for_status()  
        updated_product = response.json()
        print("---------------------")
        print("Producto actualizado con éxito")
        print(json.dumps(updated_product, indent=4, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
    except ValueError:
        print("Respuesta inválida. No se pudo parsear el JSON.")
    except Exception as e:
        print("Ha ocurrido un error:", e)

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
    opcion = input("Selecciona una opción (1-6): ")
    
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
