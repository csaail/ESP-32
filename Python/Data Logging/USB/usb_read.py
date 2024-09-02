import serial
import time

serial_port = 'COM1'
baud_rate = 115200  

ser = serial.Serial(serial_port, baud_rate)

time.sleep(2)

print("Connected to:", serial_port)

try:
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        
except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()
