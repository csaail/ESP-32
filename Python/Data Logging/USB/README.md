# USB Serial Communication Project

This repository contains scripts for reading and processing data from a USB serial port. The included files are:

## Files

1. **port_check.py**  
   This script lists all available serial ports on your machine. It's useful for identifying which port your device is connected to.

2. **usb_read.py**  
   This script establishes a serial connection to a specified port and continuously reads incoming data. It prints the data to the console.

3. **usb_csv.py**  
   This script reads data from a specified serial port, filters for lines that start with "Number," and saves the filtered data to a CSV file (`collected_data.csv`).

4. **usb.ino**  
   This Arduino sketch configures a microcontroller to send data over a serial connection. It's intended to be used with the Python scripts in this project.

## Usage

### 1. port_check.py
To identify which serial ports are available, run:
```bash
python port_check.py
