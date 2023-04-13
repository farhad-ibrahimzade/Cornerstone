#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h> // Library for the LCD

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

const int blueLED = 6;

const int redLED = 7;

const int greenLED = 5;

const int contrast = 110;

const int gameDelay = 500;

String pedestrian[4] = {"04 2B 60 A2 5C 64 81", "04 20 53 C2 5C 64 80", "04 4C 51 C2 5C 64 81", "04 F1 18 42 5D 64 80"};
String tram[4] = {"04 39 3C 42 5D 64 81", "04 52 40 42 5D 64 80", "04 EF 14 42 5D 64 80", "04 0C EF 7A 5D 64 81"};
String bus[4] = {"04 FA 41 42 5D 64 80", "04 28 60 A2 5C 64 81", "90 5F B1 26", "04 0B EF 7A 5D 64 81"}; //fixed chip: 04 B3 F2 42 5D 64 80
String bike[4] = {"04 4B EA 4A 5D 64 81", "04 57 40 42 5D 64 80", "04 53 55 C2 5C 64 81", "04 25 53 C2 5C 64 80"};
String car[4] = {"04 F2 EA BA 5C 64 80", "04 A5 EB BA 5C 64 80", "04 B1 2E 22 A8 64 80", "04 BA EC 7A 5D 64 80"};

void setup() {
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);

  digitalWrite(redLED, LOW);
  digitalWrite(greenLED, LOW);
  digitalWrite(blueLED, LOW);
  
	Serial.begin(9600);		// Initialize serial communications with the PC
	SPI.begin();			// Init SPI bus
	mfrc522.PCD_Init();		// Init MFRC522
	delay(4);				// Optional delay. Some board do need more time after init to be ready, see Readme

  digitalWrite(blueLED, HIGH);
  scanLanes();
}

void loop(){
  
}

// Check if address is of road type
bool checkType(String type[4], String address){
  return address == type[0] || address == type[1] || address == type[2] || address == type[3];
}

String getRoadType(String address){
  if(checkType(pedestrian, address)){
    return "Pedestrian";
  }
  else if(checkType(tram, address)){
    return "Tram";
  }
  else if(checkType(bus, address)){
    return "Bus";
  }
  else if(checkType(bike, address)){
    return "Bike";
  }
  else if(checkType(car, address)){
    return "Car";
  }
}

String getAddress(){
  String address= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     address.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     address.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  address.toUpperCase();

  return address.substring(1);
}

void scanLanes(){
  for(int i = 0; i < 6; i++){
    if ( ! mfrc522.PICC_IsNewCardPresent() || ! mfrc522.PICC_ReadCardSerial()) {
    // Check if new tag is present
      i--;
		  continue;
	  }
    digitalWrite(blueLED, LOW);
    //Output to Serial
    String output = getRoadType(getAddress()) + "," + String(i);
    Serial.println(output);
    digitalWrite(redLED, HIGH);

    delay(gameDelay);
    digitalWrite(redLED, LOW);
  }
  Serial.println("Done");
  digitalWrite(greenLED, HIGH);
}
