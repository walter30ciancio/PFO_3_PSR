import socket

HOST = '127.0.0.1'
PORT = 65432

def enviar_tarea(tarea):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Enviando tarea: {tarea}")
        s.sendall(tarea.encode('utf-8'))
        
        # Esperamos el resultado procesado por el worker
        data = s.recv(1024)
    print(f"Resultado del servidor: {data.decode('utf-8')}\n")

if __name__ == '__main__':
    print("--- Cliente Conectado ---")
    enviar_tarea("Generar reporte mensual")
    enviar_tarea("Comprimir imágenes de perfil")