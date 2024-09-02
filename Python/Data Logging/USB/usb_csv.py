import serial
import time
import csv

serial_port = 'COM1'
baud_rate = 115200 

# Create a serial object
ser = serial.Serial(serial_port, baud_rate)

# Allow some time for the serial connection to be established
time.sleep(2)

print("Connected to:", serial_port)

# List to store collected data
collected_data = []

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').rstrip()

        # Print the line
        print(line)

        # Filter and collect only relevant data
        if line.startswith("Number"):
            collected_data.append(line)
        
except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Close the serial port
    ser.close()

    # Save the collected data to a CSV file
    with open('collected_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write a header row if necessary
        writer.writerow(['Data'])

        # Write the collected data to the CSV
        for data in collected_data:
            writer.writerow([data])

    print("Data saved to collected_data.csv")
