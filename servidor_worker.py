import socket
import time
from concurrent.futures import ThreadPoolExecutor

HOST = '127.0.0.1'
PORT = 65432

def procesar_tarea(conn, addr):
    """Función que ejecuta cada hilo (Worker) al recibir una tarea"""
    with conn:
        print(f"Worker asignado al cliente {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            tarea = data.decode('utf-8')
            print(f"[{addr}] Procesando tarea: {tarea}")
            
            # Simulamos el tiempo de procesamiento de la tarea
            time.sleep(2) 
            
            respuesta = f"Tarea '{tarea}' completada exitosamente."
            conn.sendall(respuesta.encode('utf-8'))

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor Balanceador/Maestro escuchando en el puerto {PORT}...")
        
        # Creamos un pool de 5 hilos (Workers)
        with ThreadPoolExecutor(max_workers=5) as executor:
            while True:
                conn, addr = s.accept()
                # Delegamos la conexión entrante a un worker libre del pool
                executor.submit(procesar_tarea, conn, addr)

if __name__ == '__main__':
    iniciar_servidor()