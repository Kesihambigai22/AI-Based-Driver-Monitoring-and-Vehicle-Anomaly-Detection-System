import cv2, numpy as np, serial, time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Serial connection to ESP32
try:
    ser = serial.Serial('COM3', 115200, timeout=1)
    time.sleep(2)
except:
    ser = None

def calculate_EAR(eye_points, landmarks, w, h):
    pts = np.array([[int(landmarks[i].x*w), int(landmarks[i].y*h)]
                    for i in eye_points])
    v1 = np.linalg.norm(pts[1] - pts[5])
    v2 = np.linalg.norm(pts[2] - pts[4])
    h1 = np.linalg.norm(pts[0] - pts[3])
    return (v1 + v2) / (2.0 * h1)

LEFT_EYE  = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]
EAR_THRESH = 0.25; CONSEC_FRAMES = 20; frame_count = 0

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_img = vision.Image(image_format=vision.ImageFormat.SRGB, data=rgb)
    result = detector.detect(mp_img)
    if result.face_landmarks:
        lm = result.face_landmarks[0]
        left_ear  = calculate_EAR(LEFT_EYE,  lm, w, h)
        right_ear = calculate_EAR(RIGHT_EYE, lm, w, h)
        ear = (left_ear + right_ear) / 2.0
        if ear < EAR_THRESH:
            frame_count += 1
            if frame_count >= CONSEC_FRAMES:
                cv2.putText(frame, 'DROWSY!', (30,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 3)
                if ser: ser.write(b'1')
        else:
            frame_count = 0
            if ser: ser.write(b'0')
    cv2.imshow('Driver Monitor', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release(); cv2.destroyAllWindows()
