# USB Serial Communication

This repository contains scripts for reading and processing data from a USB serial port. The included files are:

## Files

1. **usb.ino**  
   This Arduino sketch configures a microcontroller to send data over a serial connection. It's intended to be used with the Python scripts in this project.

2. **port_check.py**  
   This script lists all available serial ports on your machine. It's useful for identifying which port your device is connected to.

3. **usb_read.py**  
   This script establishes a serial connection to a specified port and continuously reads incoming data. It prints the data to the console.

4. **usb_csv.py**  
   This script reads data from a specified serial port, filters for lines that start with "Number," and saves the filtered data to a CSV file (`collected_data.csv`).

## Usage

### 1. usb.ino
Upload the usb.ino sketch to your Arduino or compatible microcontroller. The sketch will send data over the serial connection, which can be read by the Python scripts.

### 2. port_check.py
To identify which serial ports are available, run:
```bash
python port_check.py
```
The script will list all the available serial ports.

### 3. usb_read.py
To start reading data from a serial port, specify the correct serial_port in the script, then run:
```bash
python usb_read.py
```
The script will continuously print incoming data from the specified serial port to the console.

### 4. usb_csv.py
To read and save filtered data to a CSV file, specify the correct serial_port in the script, then run:
```bash
Python usb_csv.py
```
The script will collect lines starting with "Number" and save them to collected_data.csv in the working directory.


### Requirements:
Arduino IDE for uploading the .ino sketch to your microcontroller<br>
Python 3.x<br>
pySerial library, install using:
```bash
pip install pyserial
```
