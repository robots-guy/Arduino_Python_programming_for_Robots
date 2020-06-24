/*Read a Temperature sensor via arduino using PytHon GUI and log it data
Note: Disconnect from Python IDE before uploading this sketch to your arduino
*/

//Declare variables
char  serialData;
const int sensorPin= 0; //Sensor pin connects to analog pin A0
int data;              //the variable that will hold the temperature value reading

//Setup your baudrate & arduino pins 
void setup() 
{
Serial.begin(9600); //sets the baud rate at 9600 so we can check the values the sensor is obtaining on the Serial Monitor
Serial.setTimeout(80);
}

void loop()
{
  data= analogRead(sensorPin); //the sensor takes readings from analog pin A0
  int temp = data - 546;  //adjust this value accordingly to your sensor
  Serial.println(temp); //send this data to python 
}
