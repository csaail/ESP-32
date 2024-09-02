import socket
import csv

ESP32_IP = "192.168.4.1" 
ESP32_PORT = 80

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((ESP32_IP, ESP32_PORT))

print("Connected to the ESP32")

# List to store received data
received_data = []

try:
    while True:
        # Receive data from the ESP32
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(data.strip())  # Print each line as it is received
        received_data.append(data.strip())  # Store the data in the list

except KeyboardInterrupt:
    print("Disconnected from the ESP32")

finally:
    # Close the connection when done
    client_socket.close()

    # Save the received data to a CSV file
    with open('esp32_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data"])  # Header for the CSV file
        for line in received_data:
            writer.writerow([line])  # Write each received line as a new row

    print("Data saved to esp32_data.csv")
