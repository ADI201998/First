#include<Wire.h>
#define addr 0x04
int x = 0,sum=0;

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  Wire.begin(addr);     
  Wire.onReceive(event);
  Serial.begin(9600);
}
int t=0,u=0;
// the loop routine runs over and over again forever:
void loop() {
   delay(100);              // nwait for a second
}
void event(int howmany)
{
  int t=0;
  if(t==1)
  {
    x = Wire.read();
    t=0
    u = u+1;
  }
  else if(t==0)
  {
    sum = Wire.read();
    u=u+1;
  }
  if(u==2)
  {
    t = x*256 + sum;
    
  }
  Serial.println(t);
}
