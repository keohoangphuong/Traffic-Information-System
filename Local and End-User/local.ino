  String toEnd = "LE6000";
  String toServ = "";
void setup() {
  // put your setup code here, to run once:
  Serial1.begin(9600);
  Serial.begin(9600);
 }

void loop() {
  if (Serial1.available()){
    String s = Serial1.readString();
    if (s.charAt(0)=='S'){
      toEnd = s;
      toEnd.setCharAt(0,'L');
      toEnd.setCharAt(0,'E');
    }
    else if(s.charAt(0)=='E'){
      toServ = s;
      toServ.setCharAt(0,'L');
      toServ.setCharAt(0,'S');
      Serial1.println(toServ);
    } 
  }
  Serial1.println(toEnd);
}
