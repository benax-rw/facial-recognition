int ledPin = 13; 

void setup() {
  pinMode(ledPin, OUTPUT); 
  Serial.begin(9600); // Start serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available() > 0) {
    char receivedChar = Serial.read(); // Read the incoming data
    if (receivedChar == '1') { // If '1' is received
      digitalWrite(ledPin, HIGH); // Turn on the LED
    }
    else{
      digitalWrite(ledPin, LOW); 
    }
  }
}

