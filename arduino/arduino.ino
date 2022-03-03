#define ledP 10
#define ledR 9
int potP = 0;
int valP = 0;
int potR = 0;
int valR = 0;
//int potM = 0;
//int valM = 0;

void setup() 
{
  pinMode(ledP, OUTPUT);
  pinMode(ledR, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  potP = analogRead(A1);
  valP = map(potP, 0, 1024, 0, 255);
  analogWrite(ledP, valP);
  //Serial.print("pinky value ");

  potR = analogRead(A4);
  valR = map(potR, 0, 1024, 0, 255);
  analogWrite(ledR, valR);
  //Serial.print("ring value ");


  Serial.print(valP);
  Serial.print(",");
  Serial.print(valR);
  Serial.println();

/*
  potM = analogRead(A5);
  valM = map(potM, 0, 1024, 0, 255);
  //analogWrite(ledM, valM);
  Serial.print("middle value ");
  Serial.print(valM);
  Serial.println();
  Serial.println();
*/
  delay(100);

  
  //digitalWrite(led, HIGH);
  //delay(1000);c yju 
  //digitalWrite(led, LOW);
  //delay(1000);
}
