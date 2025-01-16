# Driver-Drowsiness-Detection-Using-AI

Background
Driver drowsiness and fatigue are leading causes of road accidents, accounting for thousands of deaths and injuries annually. Traditional methods like EEG and ECG-based systems are effective but expensive and intrusive. This project leverages non-invasive AI and computer vision techniques to provide a cost-effective and efficient solution for real-time driver drowsiness detection, potentially saving lives by alerting drivers before accidents occur.

Problem Statement
Driver drowsiness is a critical factor in road accidents worldwide. Existing solutions are often expensive, lack accuracy, or delay in alerting the driver. A real-time, accurate, and cost-effective system is essential to monitor driver alertness and issue timely warnings.

Justification
This project aims to design a non-invasive, cost-efficient drowsiness detection system. Unlike previous approaches focusing only on eye closure, this system also incorporates yawning detection to improve reliability. The goal is to ensure safer roads by preventing accidents caused by drowsy driving.

Objective
General Objective
To design and implement a real-time driver drowsiness detection system that can be integrated into any vehicle, ensuring the safety of drivers and passengers.

Specific Objectives
Detect driver drowsiness by monitoring eye closure and yawning in real time.
Provide reliable performance under various lighting conditions and with or without glasses.
Issue timely audio alerts to wake up the driver upon detecting drowsiness.
Enhance road safety by reducing accidents caused by fatigue.

Proposed Solution
The system captures video streams of the driver’s face and analyzes them to detect signs of drowsiness. Key components include:

Face Detection: Locates the face in each video frame.
Eye Detection: Tracks the Eye Aspect Ratio (EAR) to determine if the eyes are closed.
Yawning Detection: Tracks the Mouth Aspect Ratio (MAR) to detect yawns.
Alert System: Issues an alarm when signs of drowsiness are detected.
The system uses OpenCV and Dlib for facial landmark detection, combined with Python for efficient processing.

