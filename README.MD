Sebastián Eli Román Álvarez 
Edwin Caleb Trejo Aguiñaga
Brandon enrique Hernández Martínez 
Gerardo Arias Magaña 
Alexandre Almaraz Mayen 
José Sebastián Colin Becerra

Descripción
    Este programa simula el funcionamiento de un restaurante en el que hay 5 mesas y 3 camareros. Cada mesa representa un cliente que hace un pedido de comida, y los camareros son responsables de atender los pedidos, prepararlos y entregarlos a las mesas correspondientes. El programa utiliza multithreading para simular la concurrencia y mejorar la eficiencia en la atención de pedidos.

Objetivo
    El objetivo de este proyecto es mostrar cómo los hilos (threads) en Python pueden realizar tareas concurrentes para optimizar el procesamiento de pedidos en un restaurante.

Funcionalidad
    Mesas (Clientes): Cada mesa representa a un cliente que solicita un pedido de comida seleccionado al azar.
    Camareros: Cada camarero trabaja en un hilo separado y es responsable de atender a los clientes, preparar los pedidos y entregarlos.
    Sincronización de Tareas: Las mesas y los camareros trabajan de forma concurrente, de modo que los camareros preparan los pedidos a medida que estos llegan y los entregan cuando están listos.
    Simulación de Tiempos: El programa utiliza time.sleep() para simular los tiempos de espera y preparación de los pedidos.
Estructura del Código
    Librerías
        threading: Para crear y manejar los hilos que simulan mesas y camareros.
        time: Para simular tiempos de espera.
        random: Para seleccionar pedidos al azar.
        queue.Queue: Para gestionar una cola de pedidos y asegurar la sincronización entre los hilos.
Funciones
    mesa(mesa_id): Representa a un cliente en una mesa que elige un pedido al azar y lo coloca en la cola de pedidos.
    camarero(camarero_id): Simula el trabajo de un camarero que toma pedidos de la cola, los prepara, y luego los entrega a la mesa correspondiente.
Flujo del Programa
    Generación de Pedidos: Se crean y ejecutan 5 hilos de mesas (clientes), cada uno de los cuales genera un pedido al azar y lo coloca en una cola de pedidos compartida.
    Atención de Pedidos: Se crean y ejecutan 3 hilos de camareros que toman los pedidos de la cola, simulan la preparación, y luego los entregan a las mesas correspondientes.
    Finalización: El programa espera a que todos los pedidos sean entregados y luego imprime un mensaje de pedidos entregados
