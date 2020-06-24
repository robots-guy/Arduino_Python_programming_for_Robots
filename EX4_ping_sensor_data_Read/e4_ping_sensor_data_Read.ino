/*Read a Ultrasonic sensor data (Ping sensor) via arduino using PytHon GUI 
Note: Disconnect from Python IDE before uploading this sketch to your arduino
*/

//Declare variables
char  serialData;

//Ping sensor pins
int trigPin = 11;    // Trigger
int echoPin = 12;    // Echo
long duration, cm;

//Setup your baudrate & arduino pins 
void setup() 
{
  //Serial Port begin
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.setTimeout(80);
}
 
void loop() 
{
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
 
  // Convert the time into a distance
  cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  Serial.println(cm); //This will be sent to python for displaying graph 
  delay(500);
}
