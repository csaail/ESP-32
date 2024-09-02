import socket

ESP32_IP = "192.168.4.1"
ESP32_PORT = 80        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((ESP32_IP, ESP32_PORT))

print("Connected to the ESP32")

try:
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(data.strip())  
      
except KeyboardInterrupt:
    print("Disconnected from the ESP32")

finally:
    client_socket.close()
