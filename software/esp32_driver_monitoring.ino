// PIN DEFINITIONS
#define ENA 14   #define IN1 26   #define IN2 27
#define IR_PIN 34   #define BUZZER 25

volatile int count = 0;
unsigned long lastTime = 0;
char driverData = '0';
int rpm = 0;

void IRAM_ATTR detect() { count++; }

void setup() {
  Serial.begin(115200);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);
  pinMode(BUZZER, OUTPUT); pinMode(IR_PIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(IR_PIN), detect, FALLING);
  ledcAttach(ENA, 5000, 8);  // PWM: 5kHz, 8-bit
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  lastTime = millis();
}

void loop() {
  if (Serial.available()) { driverData = Serial.read(); }
  if (millis() - lastTime >= 1000) {
    rpm = count * 60; count = 0; lastTime = millis();
    Serial.print("RPM: "); Serial.println(rpm);
  }
  bool anomaly = (rpm < 100 || rpm > 3000);
  bool drowsy  = (driverData == '1');
  if (drowsy || anomaly) {
    ledcWrite(ENA, 80); digitalWrite(BUZZER, HIGH);
  } else {
    ledcWrite(ENA, 200); digitalWrite(BUZZER, LOW);
  }
  delay(50);
}
