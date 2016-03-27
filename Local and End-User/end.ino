#include "LiquidCrystal.h"
int analogPin = 0;     // potentiometer wiper (middle terminal) connected to analog pin 3
int help1 = 5;
int help2 = 6;
int val = 0;           // variable to store the value read
int v = 0;
String S = "60";
int H = 0;
int E = 0;
String s;
LiquidCrystal lcd(8,9,10,11,12,13);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  Serial1.begin(9600);
  pinMode(help1,INPUT);
  pinMode(help2,INPUT);
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  v = S.toInt();
  val = analogRead(analogPin)/10;    // read the input pin
  lcd.setCursor(0, 0);
  lcd.print("Allowed v: "+ S);
  
  if (Serial1.available()){
    s = Serial1.readString();
    if (s.charAt(0)=='S'){
      S = s.substring(2,3);
      H = s.substring(4,4).toInt();
      E = s.substring(5,5).toInt();
      }
    } 
  // print the number of seconds since reset:
  
  if(val>v){
     lcd.setCursor(0, 1);
     lcd.print("overspeed!");
     lcd.setCursor(0, 1);
     lcd.print("          ");
  }
//  if(digitalRead(help1)){
//   //while(!digitalRead(help1));
//     lcd.setCursor(0, 1);
//     lcd.print("Robbery report!");
//     lcd.setCursor(0, 1);
//     lcd.print("               ");
//     Serial1.print("EL1");
 // }
  if(digitalRead(help2)){
  // while(digitalRead(help2));
     lcd.setCursor(0 , 1);
     lcd.print("Invoking assistance!");
     lcd.setCursor(0, 1);
     lcd.print("                    ");
     Serial1.print("LS2");
  }
}

