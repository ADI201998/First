/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
 
  This example code is in the public domain.
 */
 
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
#include<Wire.h>
#define addr 0x05

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Wire.begin(addr);     
  Wire.onReceive(event);
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
   delay(1);              // wait for a second
}
void event(int howmany)
{
  char x = Wire.read();
  Serial.println(x);
}
