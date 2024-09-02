#include <WiFi.h>

const char* ssid = "ESP32-Access-Point";
const char* password = "12345678";

// Create a server object that listens on port 80
WiFiServer server(80);

int counter = 1;

void setup() {
  // Start the serial communication
  Serial.begin(115200);

  // Set up the access point
  WiFi.softAP(ssid, password);

  // Start the server
  server.begin();

  Serial.println();
  Serial.print("Access Point \"");
  Serial.print(ssid);
  Serial.println("\" started");
  
  Serial.print("IP Address: ");
  Serial.println(WiFi.softAPIP());
  
  Serial.println("Waiting for client to connect...");
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (client) {
    Serial.println("Client connected!");

    while (client.connected()) {
      // Send the entire line in one go
      String message = "Number " + String(counter) + "\n";
      client.print(message);  // Send "Number X" on the same line

      // Increment the counter by 1
      counter++;

      // Wait for 1 second
      delay(1000);

      // Check if the client is still connected
      if (!client.connected()) {
        Serial.println("Client disconnected.");
        break;
      }
    }
    // Close the connection
    client.stop();
  }
}
