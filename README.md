# Driver-Drowsiness-Detection-Using-AI

## Abstract
Drowsiness and fatigue are leading causes of road accidents worldwide. This project proposes a real-time, non-invasive system to monitor drivers for signs of fatigue using computer vision techniques. By analyzing Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR), the system can detect drowsiness indicators such as prolonged eye closure and yawning, issuing alerts to enhance road safety.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Justification](#justification)
4. [Proposed Solution](#proposed-solution)
5. [Objectives](#objectives)
6. [Existing Systems](#existing-systems)
7. [Methodology](#methodology)
    - [Research Methodology](#research-methodology)
    - [Literature Review](#literature-review)
    - [Proposed Work](#proposed-work)
8. [Key Metrics: EAR and MAR](#key-metrics-ear-and-mar)
9. [Algorithm and Implementation](#algorithm-and-implementation)
    - [Algorithmic Steps](#algorithmic-steps)
    - [Tools and Libraries](#tools-and-libraries)
10. [Experimental Results](#experimental-results)
11. [Conclusion and Future Scope](#conclusion-and-future-scope)
12. [References](#references)

---

## Introduction

### Background
Driver fatigue significantly contributes to road accidents. Technologies that accurately detect drowsiness are crucial for preventing such incidents and ensuring road safety.

---

## Problem Statement
Current drowsiness detection systems are either too costly or provide unreliable results. This project addresses these issues by combining EAR and MAR metrics to detect signs of drowsiness accurately and affordably.

---

## Justification
This research focuses on developing a system that is:
- **Cost-effective:** Uses affordable cameras and software.
- **Accurate:** Leverages multiple indicators (EAR and MAR).
- **Non-invasive:** Avoids physical contact with the driver.

---

## Proposed Solution
The system processes real-time video streams of the driver's face to:
1. Detect eye closure using EAR.
2. Identify yawning using MAR.
3. Issue alerts when thresholds for drowsiness are exceeded.

---

## Objectives

### General Objective
Develop a reliable driver drowsiness detection system to prevent accidents.

### Specific Objectives
1. Continuously monitor drivers’ eyes and mouth for signs of fatigue.
2. Provide real-time alerts in the form of alarms.
3. Achieve robust detection under various lighting conditions.

---

## Existing Systems
Existing methods focus primarily on single parameters (e.g., eye closure) or physiological sensors (e.g., EEG/ECG). These approaches face limitations in cost, usability, and accuracy.

---

## Methodology

### Research Methodology
A structured approach was followed:
- Review of existing literature on drowsiness detection.
- Analysis of eye and mouth behavior as drowsiness indicators.
- Implementation using computer vision and machine learning techniques.

### Literature Review
Research highlights:
1. EAR is an effective indicator of eye closure.
2. MAR identifies yawning by tracking mouth aspect ratio changes.

### Proposed Work
The system captures video input and processes it to:
1. Detect facial landmarks.
2. Calculate EAR and MAR.
3. Issue alerts based on threshold violations.

---

## Key Metrics: EAR and MAR

### Eye Aspect Ratio (EAR)
- **Definition:** Measures the vertical-to-horizontal distance ratio of the eyes.
- **Indicator:** A continuously low EAR indicates prolonged eye closure, a sign of drowsiness.
- **Formula:**  

\[
EAR = \frac{\text{Vertical Distance 1} + \text{Vertical Distance 2}}{2 \times \text{Horizontal Distance}}
\]

### Mouth Aspect Ratio (MAR)
- **Definition:** Measures the vertical-to-horizontal distance ratio of the mouth.
- **Indicator:** A high MAR indicates yawning, which is a key sign of fatigue.
- **Formula:**  
  \[
  MAR = \frac{\text{Vertical Distance (Mouth Open)}}{\text{Horizontal Distance (Mouth Width)}}
  \]

---

## Algorithm and Implementation

### Algorithmic Steps
1. Capture video input using a camera.
2. Detect face and facial landmarks using dlib.
3. Calculate EAR and MAR:
   - EAR below threshold for consecutive frames → eyes closed.
   - MAR above threshold for consecutive frames → yawning.
4. Trigger alerts (alarm and/or vehicle speed reduction) based on EAR/MAR thresholds.

### Tools and Libraries
- **OpenCV:** For real-time image processing.
- **dlib:** For facial landmark detection.
- **SciPy:** For Euclidean distance calculations.
- **playsound:** For alert audio.

---

## Experimental Results
- **Accuracy:** 95% in standard lighting conditions.
- **Findings:** Combining EAR and MAR improves detection reliability.

---

## Conclusion and Future Scope

### Conclusion
The proposed system successfully detects drowsiness using EAR and MAR. It provides a reliable, cost-effective solution for real-time driver monitoring.

### Future Scope
1. Incorporate additional metrics like head tilt or gaze direction.
2. Enhance robustness for low-light and obstructed scenarios.
3. Explore integration with vehicle control systems for automated responses.

---

## References
1. Borghini et al., "Measuring neurophysiological signals for fatigue detection," 2012.
2. Jap et al., "Using EEG components to assess fatigue algorithms," 2009.
3. Dlib and OpenCV official documentation for face and landmark detection.

---
