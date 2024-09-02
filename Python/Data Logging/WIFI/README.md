# ESP32 Wi-Fi Communication

This repository contains scripts for reading and processing data received over Wi-Fi from an ESP32 microcontroller. The included files are:

## Files

1. **wifi.ino**  
   This Arduino sketch is designed to run on an ESP32 microcontroller. It configures the ESP32 to send data over Wi-Fi, which can be read by the Python scripts in this project.

2. **wifi_read.py**  
   This script establishes a Wi-Fi connection to an ESP32 and continuously reads incoming data. It prints the data to the console.

3. **wifi_csv.py**  
   This script connects to an ESP32 over Wi-Fi, receives data, and saves it to a CSV file (`esp32_data.csv`).

## Usage

### 1. wifi.ino
Upload the wifi.ino sketch to your ESP32 microcontroller. The sketch will send data over Wi-Fi, which can be read by the Python scripts.

### 2. wifi_read.py
To start reading data from the ESP32 over Wi-Fi, specify the correct `ESP32_IP` and `ESP32_PORT` in the script, then run:
```bash
python wifi_read.py
```
The script will continuously print incoming data from the ESP32 to the console.

### 3. wifi_csv.py
To read and save data received from the ESP32 to a CSV file, specify the correct ESP32_IP and ESP32_PORT in the script, then run:
```bash
python wifi_csv.py
```
The script will collect the received data and save it to esp32_data.csv in the working directory.


### Requirements
Arduino IDE for uploading the .ino sketch to your ESP32 microcontroller
Python 3.x
