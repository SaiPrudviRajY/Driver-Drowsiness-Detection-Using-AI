import numpy as np
import cv2
import dlib
import imutils
from imutils import face_utils
from scipy.spatial import distance as dist
from threading import Thread
import pygame
import time

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Function to play alarm sound for 3 seconds
def play_alarm():
    pygame.mixer.music.load("/Users/saiprudvirajyerrapragada/Desktop/Drowsiness Detection/alarm.wav")
    pygame.mixer.music.play()
    time.sleep(3)  # Play sound for 3 seconds
    pygame.mixer.music.stop()  # Stop playback

# Function to calculate Eye Aspect Ratio (EAR)
def calculate_EAR(eye):
    A = dist.euclidean(eye[1], eye[5])  # Vertical distance 1
    B = dist.euclidean(eye[2], eye[4])  # Vertical distance 2
    C = dist.euclidean(eye[0], eye[3])  # Horizontal distance
    EAR = (A + B) / (2.0 * C)
    return EAR

# Function to calculate Mouth Aspect Ratio (MAR)
def calculate_MAR(mouth):
    A = dist.euclidean(mouth[3], mouth[9])  # Vertical distance
    B = dist.euclidean(mouth[0], mouth[6])  # Horizontal distance
    MAR = A / B
    return MAR

# Thresholds and counters (parameters for detecting drowsiness and yawning)
EYE_AR_THRESH = 0.27  # EAR threshold for detecting eye closure
EYE_AR_CONSEC_FRAMES = 25  # Minimum consecutive frames for eye closure detection
MAR_THRESH = 0.6  # MAR threshold for detecting yawning
MAR_CONSEC_FRAMES = 8  # Minimum consecutive frames for yawn detection
COUNTER = 0  # Counter for frames with eyes closed
YAWNING = False  # Boolean state indicating if a yawn is currently in progress
LAST_YAWN_TIME = 0  # Timestamp of the last detected yawn
YAWN_COOLDOWN_TIME = 10  # Cooldown time in seconds between yawns
EVENT_COUNT = 0  # Total number of detected events (yawns + eye closures)
BREAK_REMINDER_THRESHOLD = 5  # Total event count threshold for reminding the driver to take a break

# Load Dlib's face detector and facial landmark predictor
print("[INFO] Loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("/Users/saiprudvirajyerrapragada/Desktop/Drowsiness Detection/shape_predictor_68_face_landmarks.dat")

# Landmark indices for eyes and mouth
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

# Start video stream
print("[INFO] Starting video stream...")
vs = cv2.VideoCapture(0)

while True:
    ret, frame = vs.read()
    if not ret:
        break

    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray, 0)

    for face in faces:
        # Get facial landmarks
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        # Extract eyes and mouth
        left_eye = shape[lStart:lEnd]
        right_eye = shape[rStart:rEnd]
        mouth = shape[mStart:mEnd]

        # Calculate EAR and MAR
        left_EAR = calculate_EAR(left_eye)
        right_EAR = calculate_EAR(right_eye)
        EAR = (left_EAR + right_EAR) / 2.0
        MAR = calculate_MAR(mouth)

        # Display EAR and MAR values on screen
        cv2.putText(frame, f"EAR: {EAR:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"MAR: {MAR:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"Events: {EVENT_COUNT}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Check if EAR is below threshold (Eye closure detection)
        if EAR < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                EVENT_COUNT += 1  # Increment combined event count
                COUNTER = 0  # Reset counter
                if not ALARM_ON:
                    ALARM_ON = True
                    t = Thread(target=play_alarm)
                    t.daemon = True
                    t.start()
        else:
            COUNTER = 0
            ALARM_ON = False

        # Check if MAR is above threshold (Yawning detection)
        if MAR > MAR_THRESH:
            current_time = time.time()
            if not YAWNING and (current_time - LAST_YAWN_TIME) >= YAWN_COOLDOWN_TIME:
                YAWNING = True
                LAST_YAWN_TIME = current_time  # Update last yawn time
                EVENT_COUNT += 1
                if not ALARM_ON:
                    ALARM_ON = True
                    t = Thread(target=play_alarm)
                    t.daemon = True
                    t.start()
        else:
            YAWNING = False  # Reset yawning state once the mouth is closed

        # Alert the driver to take a break if events exceed the threshold
        if EVENT_COUNT >= BREAK_REMINDER_THRESHOLD:
            cv2.putText(frame, "DROWSINESS DETECTED!", (100, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            cv2.putText(frame, "TAKE A BREAK!", (100, 250),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            if not ALARM_ON:
                t = Thread(target=play_alarm)
                t.daemon = True
                t.start()

    # Display the frame
    cv2.imshow("Driver Drowsiness Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Cleanup
cv2.destroyAllWindows()
vs.release()
