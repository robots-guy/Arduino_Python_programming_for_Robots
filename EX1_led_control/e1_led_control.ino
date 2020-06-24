/*Control an LED to be ON/OFF via arduino using PytHon GUI 
Note: Disconnect from Python IDE before uploading this sketch to your arduino
*/

//Declare variable 
char  serialData; 

//Setup your baudrate & arduino pins   
void setup()
{
    pinMode(13, OUTPUT);// LED pin on arduino
    Serial.begin(9600);
}

//Run your program again and again using loop
void loop()
{

 if (Serial.available() > 0) // send data only when you receive data from python
 {
      serialData = Serial.read();//read serial data and assign to variable 
      Serial.print(serialData); //Print to check your data

      //Condition statement 
      if(serialData == '0') 
          {
           digitalWrite(13, HIGH); //Make your LED glow
          } 
      else if(serialData == '1') 
          {
             digitalWrite(13, LOW); //Make your LED off
          } 
        
  }
}
