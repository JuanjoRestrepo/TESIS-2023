int in1 = 3;
int P2 = 12;
int in2 = 4;
int P3 = 11;
int led = 13;
bool b1;
bool b2;
// the setup routine runs once when you press reset:
void setup() {  
  Serial.begin(9600);  
  // initialize the digital pin as an output.
  pinMode(in1, INPUT_PULLUP);     
  pinMode(P3, OUTPUT);
    pinMode(in2, INPUT_PULLUP);     
  pinMode(led, OUTPUT);
  pinMode(P2, OUTPUT);
  digitalWrite(P2, HIGH);
  digitalWrite(P3, HIGH);
}

// the loop routine runs over and over again forever:
void loop() {
  b1 = digitalRead(in1);
  b2 = digitalRead(in2);
  if (b1==false){
  Serial.println("1");
  }
  
  if (b2==false){
  Serial.println("2");
  }
  
    if (Serial.available()>0) 
      {
      char option = Serial.read();
      Serial.println("OK");
      if (option == '1')
      {

        digitalWrite(P2, LOW);
        delay(3000);
        digitalWrite(P2, HIGH);
      }
      if (option == '2')
      {
        digitalWrite(P2, LOW);
        delay(3000);
        digitalWrite(P2, HIGH);
      }
      Serial.flush();
   }
}
