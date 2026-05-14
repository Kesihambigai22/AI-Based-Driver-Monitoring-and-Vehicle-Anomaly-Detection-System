# Software Implementation

This folder contains the software implementation for the AI-based driver monitoring and vehicle anomaly detection system.

## Files Included

| File | Description |
|---|---|
| drowsiness_detection.py | Python AI-based drowsiness detection |
| esp32_driver_monitoring.ino | ESP32 embedded control code |
| README.md | Software documentation |

---

# Software Modules

## Python AI Module

The Python module performs:
- Webcam frame capture
- Face landmark detection
- Eye Aspect Ratio (EAR) calculation
- Drowsiness detection
- Serial communication with ESP32

### Libraries Used

- OpenCV
- NumPy
- MediaPipe
- PySerial

---

## ESP32 Embedded Module

The ESP32 module performs:
- RPM monitoring using IR interrupts
- Serial data reception
- PWM motor speed control
- Buzzer alert activation
- Real-time safety response

---

# Software Workflow

```text
Webcam
   ↓
OpenCV Processing
   ↓
MediaPipe Landmark Detection
   ↓
EAR Calculation
   ↓
Drowsiness Decision
   ↓
Serial Communication
   ↓
ESP32
   ↓
RPM Monitoring
   ↓
Motor Control + Alert
