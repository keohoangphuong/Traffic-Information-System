void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
  Serial.begin(9600);
 // Serial1.write(33);
}
char  a = 2;
void loop() {
  // put your main code here, to run repeatedly:
//  if (Serial1.available()){
//    a = Serial1.read();
//    Serial.write(a,DEC);
//  }
//  if (Serial.available()){
//    a = Serial.read();
    Serial1.print(a,1);
    delay(1);
//  }  

}
