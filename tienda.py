import os
import time

inventario = []

def agregar_inventario():
    nombre = input("Agregue el nombre del producto:")
    precio = float(input("Precio del producto:"))
    cantidad =  int(input("Cantidad del producto: ")) 
    
    producto ={
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print("\nProducto agregado al inventario")
    time.sleep (3)
    os.system("cls")
    menu()

def eliminar():
    nombre = input("nombre del producto a eliminar:")
    for producto in inventario:
        if producto["nombre"] == nombre:
            inventario.remove(producto)
            print("\nProducto eliminado")
            time.sleep(3)
            os.system("cls")
            menu()
            
def mostrar_inventario():
  if not inventario:
    print("No hay productos en el inventario.")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()
    

  print("Productos en el inventario:")
  for producto in inventario:
    print(f"- {producto['nombre']}: ${producto['precio']} (Cantidad: {producto['cantidad']})")
  time.sleep(3)
  os.system('cls' if os.name == 'nt' else 'clear')
  menu()


def menu():
  """Menu princiapl"""
  while True:
    print("\nMenú de tienda:")
    print("1. agregar producto")
    print("2. eliminar producto")
    print("3. mostrar inventario")
    print("4. salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        agregar_inventario()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        mostrar_inventario()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")

menu()