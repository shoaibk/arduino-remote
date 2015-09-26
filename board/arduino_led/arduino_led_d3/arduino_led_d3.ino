/**
 * Setup:
 * Connect an LED to digital pin 3
 * 
 * Description:
 * Control the LED using serial input
 * '1' => ON
 * '0' => OFF
 * 
 * E.g., after uploading this sketch, open the terminal on your host computer, and type:
 * 
 * cat > /dev/cu.usbmodemxxxx (where xxxx is the port assigned. check the exact port number using ls /dev/cu.usbmodem*)
 * 1 (Return) turns the LED ON 
 * 0 (Return) turns the LED OFF
 * 
 */
const int pinLed = 3;
char input = '0';


void setup() {
  // put your setup code here, to run once:
  pinMode(pinLed, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  input = Serial.read();
  //Serial.println(input);

  if(input == '1') {
    blink();
    turnOn();
  }

  if(input == '0') {
    blink();
    turnOff();
  }
  
  delay(500);
}

void blink() {
  for(int i = 0; i < 3; i++) {
    digitalWrite(pinLed, HIGH); 
    delay(100);
    digitalWrite(pinLed, LOW); 
    delay(100);
  } 
}

void turnOn() {
  digitalWrite(pinLed, HIGH);
}

void turnOff() {
  digitalWrite(pinLed, LOW);
}

