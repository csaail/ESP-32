# Device Specifications

## Processors
- **CPU**: Xtensa dual-core (or single-core) 32-bit LX6 microprocessor
  - Operating at 160 or 240 MHz
  - Performance: Up to 600 DMIPS
- **Ultra Low Power (ULP) Co-Processor**: Integrated for power-efficient operations

## Memory
- **SRAM**: 520 KiB

## Wireless Connectivity
- **Wi-Fi**: 802.11 b/g/n
- **Bluetooth**: v4.2 BR/EDR and BLE (shares the radio with Wi-Fi)

## Peripheral Interfaces
- **12-bit SAR ADC**: Up to 18 channels
- **2 × 8-bit DACs**
- **10 × Touch Sensors**: Capacitive sensing GPIOs
- **4 × SPI Interfaces**
- **2 × I²S Interfaces**
- **2 × I²C Interfaces**
- **3 × UART Interfaces**
- **SD/SDIO/CE-ATA/MMC/eMMC Host Controller**
- **SDIO/SPI Slave Controller**
- **Ethernet MAC Interface**: With dedicated DMA and IEEE 1588 Precision Time Protocol support
- **CAN Bus 2.0**
- **Infrared Remote Controller**: TX/RX, up to 8 channels
- **Motor PWM**
- **LED PWM**: Up to 16 channels
- **Hall Effect Sensor**
- **Ultra Low Power Analog Pre-Amplifier**

## Security Features
- **IEEE 802.11 Standard Security**: WFA, WPA/WPA2, and WAPI supported
- **Secure Boot**
- **Flash Encryption**
- **1024-bit OTP**: Up to 768-bit for customers
- **Cryptographic Hardware Acceleration**:
  - AES
  - SHA-2
  - RSA
  - Elliptic Curve Cryptography (ECC)
  - Random Number Generator (RNG)

## Power Management
- **Internal Low-Dropout Regulator**
- **Individual Power Domain**: For RTC
- **Deep Sleep Current**: 5μA
- **Wake Up Sources**:
  - GPIO interrupt
  - Timer
  - ADC measurements
  - Capacitive touch sensor interrupt

## Pinout Description

![ESP32-DOIT-DEV-KIT-v1-pinout-mischianti](https://github.com/user-attachments/assets/b90570a8-e2a3-48ce-93a4-06126da2ac00)


The DoIt ESP32 DevKit V1 features a comprehensive pinout that caters to a wide range of functionalities. Here’s a brief overview of its pinout:

- **GPIO Pins**: The board provides numerous General Purpose Input/Output (GPIO) pins which can be used for various digital input/output functionalities. These pins also support additional features like PWM, I2C, SPI, and more.

- **Analog Inputs**: Several pins on the ESP32 DevKit V1 are capable of reading analog signals, making them suitable for interfacing with analog sensors.

- **3.3V and GND Pins**: These are used to power external components or sensors.

- **5V and GND**: The board can also provide a 5V output, which is useful for powering external modules that require more power.

- **VIN**: This is the input voltage pin, which can be used to power the board when not using the USB connection.

- **EN**: This is the enable pin. It’s used to reset the microcontroller.

- **TX/RX**: These pins are used for serial communication.

- **SPI Interface**: The board has pins for SPI communication, enabling fast data transfer with peripherals like displays or flash memory.

- **I2C Interface**: The ESP32 DevKit V1 supports I2C communication, which is widely used for interfacing with sensors and other peripherals.

- **Touch Sensor Pins**: Some GPIOs can be used as capacitive touch inputs, offering an interface for touch-based input devices.

- **VP/VN**: These are the pins for the internal hall effect sensor.

- **USB-to-UART Bridge**: This feature is crucial for programming the ESP32 using a USB cable and also for serial communication with a computer or other USB host devices.

This board’s flexibility with various protocols and interfaces makes it ideal for a wide range of IoT and embedded system applications.
