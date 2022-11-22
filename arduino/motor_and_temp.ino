int var;
int analog = A1;
int temp = 0;
String inputString = "";
boolean stringComplete = false;
void setup() {
  pinMode(analog, INPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  Serial.begin(9600);
  while(!Serial){
    ;
    }
    while(Serial.available()<=0){
      sendTemp();
      delay(500);
      }
}

void loop() {
  
  if(stringComplete){
    if(inputString.startsWith("status")){
      sendTemp();
    }
    else if(inputString.startsWith("set")){
      if (inputString.indexOf("on") > -1){
      digitalWrite(23,HIGH);
      Serial.println("encendio el led");
      }
      else if(inputString.indexOf("off") > -1) {
        digitalWrite(23,LOW);
      Serial.println("apago el led");
      }
      else {
        Serial.println("comando set invalido");
      }
    }
    else{
       Serial.println("comando invalido");
    }
    stringComplete = false;
    inputString = "";
  }
delay(10);
}

void sendTemp(){
  char buffer[50];
  temp = analogRead(analog);
  temp = (temp*500)/1023;
  sprintf (buffer, "%d", temp);
  Serial.println(buffer);
}

void serialEvent() {
  while (Serial.available()){
    char inChar = (char)Serial.read();
    inputString += inChar;
    if(inChar == '\n') {
      stringComplete = true;
      }
  }
}
