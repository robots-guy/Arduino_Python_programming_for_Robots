/*control a RGB Led via arduino using PytHon GUI 
Note: Disconnect from Python IDE before uploading this sketch to your arduino
Based on your RGB LED config, connect cathode or anode accordingly to +5V or Gnd
*/

//Declare variables
int incomingByte = 0; // for incoming serial data
String myString;
long myStringInt = 0;

//Set RGB led pins. Mke sure its connected to PWM pins of arduino 
int redPin   = 9; //Red led connected to arduino PWM pin
int greenPin = 10; //green led connected to arduino PWM pin
int bluePin  = 11; //blue led connected to arduino PWM pin

//Setup your baudrate & arduino pins 
void setup() 
{
  pinMode(redPin,   OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin,  OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);  // improves the serial response time
  
  //set initial color of your LED to red
  analogWrite(redPin, 0);
  analogWrite(greenPin, 255);
  analogWrite(bluePin, 255);
}

void loop() 
{

  myString = getSerial(); //get serial functions gets the data from python
  
  if (myString.startsWith("#"))    
  { 
    String value;
    myString.remove(0, 1);      // removes "#" to only have the numbers
    Serial.println(myString);   // print this value for cross-checking
    char charbuf[8];
    myString.toCharArray(charbuf,8);
    long int rgb= strtol(charbuf,0,16); //=>rgb=0x001234FE;

    //Convert values for red, green, blue from hex value 
    byte r=(byte)(rgb>>16);
    byte g=(byte)(rgb>>8);
    byte b=(byte)(rgb);

    //Set your RGB led to respective analog value 
    Serial.println(r); // print this value for cross-checking
    Serial.println(g); // print this value for cross-checking
    Serial.println(b); // print this value for cross-checking

    //As LED's are connected to PWM pins, you need to subtract from 255 
    // (255, 0, 0) --> RED color is mapped --> (0,255,255) for PWM pins
    analogWrite(redPin, 255-r); //Subtract value from 255 as its PWM pin 
    analogWrite(greenPin, 255-g);
    analogWrite(bluePin, 255-b);
  }
}

//function to get data from python 
String getSerial()  
{
  String a;
  while (Serial.available())   
  {   
    a = Serial.readString();
    Serial.println(a);
    return (a);
  }
}
