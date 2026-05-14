#  Results and Demonstration

This folder contains the project demonstration video and implementation snapshots.

## Files Included

| File | Description |
|---|---|
| demo.mp4 | Project demonstration video |
| setup.png | Hardware setup image |
| README.md | Results documentation |

---

# Demonstration Overview

The demo shows:
- Real-time driver monitoring
- Eye Aspect Ratio (EAR) calculation
- RPM monitoring using IR sensor
- Serial communication between Python and ESP32
- Automatic buzzer alert activation
- PWM-based motor speed reduction

---

# Test Conditions

## Normal State
- Driver alert
- RPM within safe range
- Motor runs normally
- Buzzer OFF

## Drowsiness Detection
- EAR below threshold
- Alert activated
- Motor speed reduced

## RPM Anomaly
- RPM below 100 or above 3000
- Safety response triggered

---

# Performance Results

| Parameter | Result |
|---|---|
| Drowsiness Detection Latency | ~0.7 sec |
| RPM Accuracy | ±5 RPM |
| Serial Baud Rate | 115200 |
| Detection Type | Real-time |

---

# Result Highlights

 Real-time AI detection  
 Stable serial communication  
 Fast alert response  
 Embedded safety system  
 Low-cost implementation

---

# Demo Files

- `demo.mp4`
- `setup.png`
