#include <Arduino.h>

int counter = 1; // Initialize a counter variable

void setup() {
  // Initialize serial communication at a baud rate of 115200
  Serial.begin(115200);

  // Print an initial message to the console
  Serial.println("Starting the count...");
}

void loop() {
  // Print the current value of the counter
  Serial.print("Number ");
  Serial.println(counter);

  // Increment the counter by 1
  counter++;

  // Wait for 1 second (1000 milliseconds)
  delay(1000);
}
