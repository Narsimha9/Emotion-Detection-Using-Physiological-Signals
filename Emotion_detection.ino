#define USE_ARDUINO_INTERRUPTS true
#include <PulseSensorPlayground.h>
const int PulseWire = 0;
const int LED13 = 13;
float temp=0;
int Threshold = 550; 
PulseSensorPlayground pulseSensor;

int sensorValue=0;
int gsr_average=0;
unsigned long int milli_time;  

void setup(){
  Serial.begin(9600);
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);
  pulseSensor.setThreshold(Threshold); 
//  if (pulseSensor.begin())
}

void loop()
{
    Serial.println("We created a pulseSensor Object !");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  

  Serial.println("LABEL,Computer Time,Time (Milli Sec.),GSR,BPM,Temperature,EMOTIONAL AFFIRM"); 
  
  const int GSR=A1;
  long sum=0;
  int myBPM = pulseSensor.getBeatsPerMinute();
  int flag=0;
  for(int i=0;i<10;i++)           //Average the 10 measurements to remove the glitch
      {
      sensorValue=analogRead(GSR);
      sum += sensorValue;
      delay(5);
      }

   gsr_average = sum/10;
   if(gsr_average<600 && (myBPM>=65 && myBPM<=135))
   {
   milli_time = millis();
   Serial.print("DATA, TIME, ");
   delay(110);
   Serial.print(milli_time);
   Serial.print(",");
   
   Serial.print(gsr_average);
   Serial.print(",");
      Serial.print(myBPM);
   Serial.print(",");
   
  temp=analogRead(A3);
  temp=temp*0.48828125;
  Serial.print(temp); 
  
  Serial.print(",");
  
   if(((myBPM>=85&&myBPM<=125)&&(gsr_average>=350&&gsr_average<599))||(myBPM>=85&&myBPM<=125))
     Serial.print("HAPPY");
   else if(((myBPM>=80&&myBPM<=90)&&(gsr_average>=300&&gsr_average<=380))||(myBPM>=80&&myBPM<=90))
     Serial.print("SAD");

    else if(myBPM>=65&&myBPM<=79)
     Serial.print("RELAXED");
     
   else if(myBPM>=125)
    Serial.print("ANGRY");
  
     
    Serial.println();
    //delay(5);
     
   }
}
