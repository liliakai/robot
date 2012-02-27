const int sensorPin = 0;    // select the input pin for the potentiometer
const int powerswitch = 12;      // select the pin for the LED
const int forward = 5;
const int backward = 6;
const int left = 10;
const int right = 11;

const int lowtime = 25;  //seconds of low voltage = turn off
const int readrate = 1000;  //milliseconds between battery readings

int voltage,count;  // variable to store the value coming from the sensor
boolean power = 1;
unsigned long timenow,lastime;
byte inByte;

void setup() {
  // declare the power as an OUTPUT:
  pinMode(powerswitch, OUTPUT);
  pinMode(sensorPin, INPUT);
  Serial.begin(57600);
  digitalWrite(powerswitch, power);
}

void loop() {
  timenow = millis();
  if (timenow - lastime >= readrate) {
  lastime = timenow;
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
  }
  if (Serial.available() > 0) {
    inByte = Serial.read();
    Serial.print("Aloha");
    Serial.println(inByte);
  }
}




