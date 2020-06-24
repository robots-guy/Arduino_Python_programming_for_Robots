/*Control Servo motor via arduino using PytHon GUI 
Note: Disconnect from Python IDE before uploading this sketch to your arduino
*/

//Include servo library
#include <Servo.h>
Servo myservo; 

//Declare variables
String inByte;
int pos;

//Setup your baudrate & arduino pins 
void setup() 
{
  myservo.attach(11);     //Digital pin that your servo is attached 
  Serial.setTimeout(80);  //time in which Serial port will wait for serail data
  Serial.begin(9600);
}

void loop()
{    
        // send data only when you receive data from python
        while (Serial.available() > 0) 
        {
                // read the incoming byte:
                String c = Serial.readString();
                //Convert string to integer 
                pos = c.toInt();
                delay(2); 
                // Print your value back
                Serial.print("C is ");
                myservo.write(pos);
                Serial.println(pos);

        }
}
