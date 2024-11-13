import threading
import time
import random
from queue import Queue

# Opciones de comida
menu = ["Pizza", "Hamburguesa", "Pasta", "Sándwich", "Ensalada"]

# Número de mesas y camareros
num_mesas = 5
num_camareros = 3

# Cola para los pedidos
pedidos = Queue()

# Función para simular las mesas que hacen pedidos
def mesa(mesa_id):
    pedido = random.choice(menu)  # Selecciona un pedido al azar
    print(f"Mesa {mesa_id}: Pedido de {pedido}")
    pedidos.put((mesa_id, pedido))  # Encola el pedido
    time.sleep(random.uniform(0.5, 1.5))  # Tiempo de espera antes de hacer el pedido

# Función para que los camareros procesen y entreguen pedidos
def camarero(camarero_id):
    while not pedidos.empty():  # Mientras haya pedidos en la cola
        mesa_id, pedido = pedidos.get()
        print(f"Camarero {camarero_id}: Preparando pedido de {pedido} para la mesa {mesa_id}")
        time.sleep(5)  # Tiempo simulado para preparar el pedido
        print(f"Camarero {camarero_id}: Entregando pedido de {pedido} a la mesa {mesa_id}")
        pedidos.task_done()  # Marca el pedido como completado en la cola

# Crear y lanzar hilos para las mesas
mesas_threads = []
for i in range(1, num_mesas + 1):
    t = threading.Thread(target=mesa, args=(i,))
    mesas_threads.append(t)
    t.start()

# Espera a que todos los hilos de las mesas terminen de hacer pedidos
for t in mesas_threads:
    t.join()

# Crear y lanzar hilos para los camareros
camareros_threads = []
for i in range(1, num_camareros + 1):
    t = threading.Thread(target=camarero, args=(i,))
    camareros_threads.append(t)
    t.start()

# Espera a que todos los pedidos sean procesados
for t in camareros_threads:
    t.join()

print("Todos los pedidos han sido entregados.")
