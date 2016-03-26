void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
  Serial.begin(9600);
  delay(2000);
}
String a;
void loop() {
 if(Serial.available()){
      a = Serial.readString();
       Serial1.print(a);
      }
      if(Serial1.available()){
      a = Serial1.readString();
       Serial.print(a);
      }
}
