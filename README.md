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
