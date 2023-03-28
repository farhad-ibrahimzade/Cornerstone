#include <SPI.h>
#include <MFRC522.h>
#include <LiquidCrystal.h> // Library for the LCD

LiquidCrystal lcd(A5, A4, A3, A2, A1, A0); // Initializing the LCD object

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

const int contrastPin = 6;

const int contrast = 110;

const int gameDelay = 1000;

String green[2] = {"04 4C 51 C2 5C 64 81", "04 F1 18 42 5D 64 80"};
String pedestrian[2] = {"04 2B 60 A2 5C 64 81", "04 20 53 C2 5C 64 80"};
String tram[2] = {"04 39 3C 42 5D 64 81", "04 52 40 42 5D 64 80"};
String bus[2] = {"04 FA 41 42 5D 64 80", "04 28 60 A2 5C 64 81"};
String bike[2] = {"04 4B EA 4A 5D 64 81", "04 57 40 42 5D 64 80"};
String car[2] = {"04 F2 EA BA 5C 64 80", "04 A5 EB BA 5C 64 80"};

void setup() {
  analogWrite(contrastPin, contrast);
  lcd.begin(16, 2); // Initialize the 16x2 LCD
	lcd.clear();	// Clear any old data displayed on the LCD
  lcd.print("Lane type:");
	Serial.begin(9600);		// Initialize serial communications with the PC
	SPI.begin();			// Init SPI bus
	mfrc522.PCD_Init();		// Init MFRC522
	delay(4);				// Optional delay. Some board do need more time after init to be ready, see Readme

  scanLanes();
}

void loop(){
  
}

// Check if address is of road type
bool checkType(String type[2], String address){
  return address == type[0] || address == type[1];
}

String getRoadType(String address){
  if(checkType(green, address)){
    return "Green";
  }
  else if(checkType(pedestrian, address)){
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

    //Output to Serial
    String output = getRoadType(getAddress()) + "," + String(i);
    Serial.println(output);

    //Output to LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Lane type:");
    lcd.setCursor(0, 1);
    lcd.print(getRoadType(getAddress()));

    delay(gameDelay);
  }
  Serial.println("Done");
}
