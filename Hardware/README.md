# Hardware Setup – AI-Based Driver Monitoring and Vehicle Anomaly Detection System

This document explains the hardware components, circuit connections, and working setup used in the project.

---

# Hardware Components

| Component | Quantity | Purpose |
|---|---|---|
| ESP32 Dev Board | 1 | Main microcontroller |
| Webcam | 1 | Captures driver face |
| IR Sensor Module | 1 | Detects motor RPM |
| DC Motor | 1 | Simulates vehicle rotation |
| L298N Motor Driver | 1 | Controls motor speed |
| Active Buzzer | 1 | Audio warning system |
| Breadboard | 1 | Circuit prototyping |
| Jumper Wires | Multiple | Connections |
| USB Cable | 1 | ESP32 programming + power |
| Laptop/PC | 1 | Runs AI detection software |

---

# Power Requirements

| Device | Voltage |
|---|---|
| ESP32 | 5V USB |
| IR Sensor | 3.3V |
| L298N Motor Driver | 5V–12V |
| DC Motor | 5V |
| Buzzer | 3.3V/5V |

---

# Pin Connections

---

# IR Sensor → ESP32

| IR Sensor Pin | ESP32 Pin |
|---|---|
| VCC | 3.3V |
| GND | GND |
| OUT | GPIO 34 |

### Function
The IR sensor detects slots in the rotating disc and generates pulses for RPM calculation.

---

# Buzzer → ESP32

| Buzzer Pin | ESP32 Pin |
|---|---|
| Positive (+) | GPIO 25 |
| Negative (-) | GND |

### Function
The buzzer activates during:
- Driver drowsiness
- RPM anomaly detection

---

# L298N Motor Driver → ESP32

| L298N Pin | ESP32 Pin |
|---|---|
| ENA | GPIO 14 |
| IN1 | GPIO 26 |
| IN2 | GPIO 27 |

### Function
The ESP32 controls motor speed using PWM signals through the L298N driver.

---

# DC Motor → L298N

| Motor Wire | L298N |
|---|---|
| Terminal 1 | OUT1 |
| Terminal 2 | OUT2 |

### Function
The motor simulates vehicle wheel/engine rotation.

---

# Hardware Working Flow

```text
Webcam
   ↓
Python AI Detection
   ↓
Serial Communication
   ↓
ESP32
   ↓
IR Sensor RPM Monitoring
   ↓
Decision Logic
   ↓
Motor Control + Buzzer Alert
