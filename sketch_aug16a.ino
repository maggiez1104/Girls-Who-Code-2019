int piezoPin = 9;

#define NOTE_C4  262
#define NOTE_CS4 277
#define NOTE_D4  294
#define NOTE_DS4 311
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_FS4 370
#define NOTE_G4  392
#define NOTE_GS4 415
#define NOTE_A4  440
#define NOTE_AS4 466
#define NOTE_B4  494
#define NOTE_C5  523
#define NOTE_CS5 554
#define NOTE_D5  587
#define NOTE_DS5 622
#define NOTE_E5  659
#define NOTE_F5  698
#define NOTE_FS5 740
#define NOTE_G5  784
#define NOTE_GS5 831
#define NOTE_A5  880
#define NOTE_AS5 932
#define NOTE_B5  988
#define NOTE_C6  1047
#define NOTE_CS6 1109
#define NOTE_D6  1175
#define NOTE_DS6 1245
#define NOTE_E6  1319
#define NOTE_F6  1397
#define NOTE_FS6 1480
#define NOTE_G6  1568
#define NOTE_GS6 1661
#define NOTE_A6  1760
#define NOTE_AS6 1865
#define NOTE_B6  1976


/*int leftWhisker = 6;
int rightWhisker = 9;
int LED = 2;
*/
int PressurePin = A0;
int force;

int i = 0;
int drink = 0;
boolean drinkenough = true;
boolean sittingtoolong = false;
boolean sign = false;
void reset () {
  drinkenough = true;
  sittingtoolong = false;
  sign = false;
}


 

void setup() {
  Serial.begin(9600);
  /*pinMode(leftWhisker, INPUT);
  pinMode(rightWhisker, INPUT);
  pinMode(LED, OUTPUT);*/
  pinMode(piezoPin, OUTPUT);
}


// notes in the melody:
int melody[] = {
  NOTE_AS4, NOTE_C5, NOTE_D5, NOTE_DS5, NOTE_D5, 0, NOTE_D5, NOTE_C5,
  NOTE_AS4, NOTE_GS4, NOTE_AS4, NOTE_G4
};

int noteDurations[] = {
  510, 510, 510, 1530, 510, 30, 510, 510, 510, 510, 1020, 1020
};

void raisemeup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 12; thisNote++) {

    int noteDuration = noteDurations[thisNote];
    tone(piezoPin, melody[thisNote], noteDuration);
    delay(noteDuration);
    // stop the tone playing:
    noTone(piezoPin);
  }
}

int melody2[] = {
  NOTE_G5, 0, NOTE_G5, 0, NOTE_G5, 0, NOTE_G5, 0, NOTE_G5, 0, NOTE_G5, 0,
  NOTE_G5, 0, NOTE_G5, NOTE_E5, 0, NOTE_E5, NOTE_G5, NOTE_E5, NOTE_G5, NOTE_A5
};

// note durations: 340 = quarter note, 8 = eighth note, etc.:
int noteDurations2[] = {
  232, 30, 232, 30, 232, 30, 348, 30, 348, 30, 348,
  30, 348, 30, 232, 232, 116, 232, 232, 232, 464, 464
};

void raiseyourglass() {
    for (int thisNote2 = 0; thisNote2 < 22; thisNote2++) {

    int noteDuration2 = noteDurations2[thisNote2];
    tone(piezoPin, melody2[thisNote2], noteDuration2);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    //int pauseBetweenNotes = 400 ;
    delay(noteDuration2);
    // stop the tone playing:
    noTone(piezoPin);
}
  
}


void loop() {
 /* int leftValue = digitalRead(leftWhisker);
  int rightValue = digitalRead(rightWhisker);
 Serial.println("This is the right value!" );
 Serial.println(rightValue);
 Serial.println("");
 delay(1000);
*/
force = analogRead(PressurePin);
Serial.print("Force is: ");
Serial.println(force);

if (drink > 3) {
      sittingtoolong = false;
       //digitalWrite(LED, LOW);
       Serial.println("Good job! You drank water! ");
       drinkenough = true;
    }

//if (rightValue == 0 && standenough == false && sittingtoolong == true) 
if (force > 200 && drinkenough == false && sittingtoolong == true) {
    raiseyourglass();
    Serial.print("Keep drinking!");
    Serial.println("");
    delay(500);
}

//else if (rightValue == 0)  
else if (force > 200) {
    Serial.print("Water has been sitting for: ");
    drink = 0;
    i = i + 1;
    Serial.print(i);
    Serial.print(" seconds!");
    Serial.println("");
    delay(1000);
      reset();
   
    if (i > 9){
      //digitalWrite(LED, HIGH);
      raisemeup();
      i = i + 8;
      sittingtoolong = true;
      Serial.println("You are dehydrated! Drink water now!");
      
      
      
    }

  }
//else if (rightValue == 1) {
else if (force < 200) {
  i = 0;
  drinkenough = false;
  //digitalWrite(LED, LOW);
  
  Serial.print("Drinking for: ");
  drink = drink + 1;
  Serial.print(drink);
  Serial.print(" seconds!");

  Serial.println("");
  delay(1000);
}
}
