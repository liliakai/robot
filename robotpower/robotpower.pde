int sensorPin = 0;    // select the input pin for the potentiometer
int powerswitch = 12;      // select the pin for the LED
int voltage,count;  // variable to store the value coming from the sensor
const int lowtime = 25;  //seconds of low voltage = turn off
boolean power = 1;

void setup() {
  // declare the power as an OUTPUT:
  pinMode(powerswitch, OUTPUT);  
  pinMode(sensorPin, INPUT);
  Serial.begin(57600);
  digitalWrite(powerswitch, power);
}

void loop() {
  voltage = analogRead(sensorPin);    
  Serial.print("Aloha");
  Serial.println(voltage);
  if (power == 1) {
    if (voltage < 180) count -= 1;
    if (voltage > 190) count = lowtime;
    if (count < 1) {
      count = 0; 
      power = 0;
      digitalWrite(powerswitch, power);
    }
  }
  if (power == 0) 
    if (voltage > 230) {
      power = 1;
      digitalWrite(powerswitch, power);
      count = lowtime;
    }
  delay(100);                  
}



