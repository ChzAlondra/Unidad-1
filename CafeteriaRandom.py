import random

# -------------------------------
# Definimos la pila como lista
# -------------------------------
pila = []

# Productos disponibles
productos = ["Torta", "Sandwich", "Dobladita"]

# -------------------------------
# Funciones para manejar la pila
# -------------------------------
def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    if not es_pila_vacia(pila):
        return pila.pop()
    else:
        return None

def es_pila_vacia(pila):
    return len(pila) == 0

# -------------------------------
# Programa principal
# -------------------------------
def cafeteria_pila():
    # Pedir cantidad de personas que llegan
    n = int(input("¿Cuántas personas llegaron a la cafetería?: "))

    # Insertar cada persona con su producto en la pila
    for i in range(1, n+1):
        indice = random.randint(0, 2)   # número aleatorio entre 0 y 2
        prod = productos[indice]
        cliente = {"Nombre": f"Cliente {i}", "Producto": prod}
        apilar(pila, cliente)
        print(f"{cliente['Nombre']} compró: {cliente['Producto']}")

    # Mostrar pila en orden LIFO (último en entrar, primero en salir)
    print("\n--- Atendiendo clientes en orden LIFO ---")
    while not es_pila_vacia(pila):
        cliente = desapilar(pila)
        print(f"Atendiendo -> {cliente['Nombre']} | Producto: {cliente['Producto']}")

# -------------------------------
# Ejecutar el programa
# -------------------------------
cafeteria_pila()
