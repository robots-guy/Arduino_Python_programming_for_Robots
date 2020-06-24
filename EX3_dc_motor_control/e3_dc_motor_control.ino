/*Control a 4-wheeled robot via arduino using PytHon GUI 
Note: Disconnect from Python IDE before uploading this sketch to your arduino
Based on your motor driver variables ceclared below may vary. But the logic still holds the same
*/

//Declare variables
char  serialData;

//Declaring Pins of arduino to pins of Deek robot 2 Channel motor driver (L293D)
//Play around your driver to control the direction of motors
int m1=6; //connects to IN2 pin of Deek Robot motor driver -->Sets the direction 
int m2=9; //Connects to IN1 pin of Deek Robot motor driver --> Sets the direction
int e1=5; //Connects to EN1 pin of Deek Robot motor driver -->Sets the speed

int x =0; //Variable to store the speed value from Python

//Setup your baudrate & arduino pins 
void setup() 
  {
       pinMode(m1, OUTPUT);
       pinMode(m2, OUTPUT);
       pinMode(e1, OUTPUT);
       Serial.begin(9600);
    }
    
void loop() 
{
    // send data only when you receive data from python
    if (Serial.available() > 0) 
    {
      serialData = Serial.read();
      Serial.print(serialData);
      
      //Clock wise rotation of motor
      if(serialData == '1') 
      {
        //Set the speed
        analogWrite(e1, x);
        //Clock wise rotation
        digitalWrite(m2, 0);
        digitalWrite(m1, 1); 
       } 
       
       //Anti-Clock wise rotation of motor
        else if (serialData == '2') 
        {
         //Set the speed
         analogWrite(e1, x);
         //Anti-Clock wise rotation
         digitalWrite(m2, 1);
         digitalWrite(m1, 0); 
        } 
        
        //Stop your motor
        else if (serialData == '3') 
        {
         digitalWrite(m1, 0);
         digitalWrite(m2, 0); 
        } 
        
        //set Speed level 1
        else if (serialData == '4') 
        {
          x=80;
        } 
        
        //set Speed level 2
        else if (serialData == '5') 
        { 
          x=150;
        }
        //set Speed level 3
        else if (serialData == '6') 
        { 
          x=255;
        }
    
    }
}
