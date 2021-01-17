int output = 0;
int OUTPUTPIN = 3; 

void setup() {
  pinMode(OUTPUTPIN, OUTPUT);
}

void loop() {
  for(output=0; output<=255; output++){
    analogWrite(3, output);
    delay(5);
    }
  delay(1000);
  for(output=255; output>=0; output--){
    analogWrite(3, output);
    delay(5);
    }

}
