# Advanced Detection Walking Stick

### Raspberry Pi-Based Obstacle Detection with Haptic Feedback

A prototype assistive technology system that detects nearby obstacles using two ultrasonic sensors and provides variable-intensity vibration feedback.

**University of Houston–Clear Lake | November 2025**

**Technologies:** Python, Raspberry Pi Zero, HC-SR04, GPIO, PWM, Circuit Design

---

## Project Overview

The Advanced Detection Walking Stick is an academic engineering project designed to explore obstacle detection and tactile feedback for individuals with visual impairments.

Our team developed a walking-stick prototype that uses two ultrasonic sensors to detect nearby objects.

The system calculates obstacle distances and adjusts vibration intensity based on proximity.

As an object approaches the sensors, the vibration command increases.

The prototype operates locally without requiring an internet connection.

---

## Demonstration

## Project Demonstration

[![Watch the Walking Stick Demonstration](https://img.youtube.com/vi/aeFKVFRX7Ho/hqdefault.jpg)](https://youtu.be/aeFKVFRX7Ho)

**[▶ Watch the Full Demonstration on YouTube](https://youtu.be/aeFKVFRX7Ho)**

This video demonstrates our team's Raspberry Pi-based obstacle-detection walking stick, which uses two ultrasonic sensors to detect nearby objects and adjusts vibration intensity based on obstacle proximity.

The system was developed using Python, GPIO, and PWM-controlled haptic feedback.

---

## Project Features

- Dual ultrasonic sensor obstacle detection
- Real-time distance calculations
- PWM-controlled vibration feedback
- Closest-obstacle prioritization
- Sensor timeout handling
- Portable Raspberry Pi-based prototype
- Operation without an internet connection

---

## Hardware Components

| Component | Purpose |
|-----------|---------|
| Raspberry Pi Zero | Main processing unit |
| 2x HC-SR04 | Ultrasonic obstacle detection |
| Vibration motor(s) | Tactile feedback |
| Transistor | Motor-driving circuit |
| 10 kΩ resistor | Motor driver circuit |
| Breadboard | Circuit assembly |
| Power bank | Portable power source |
| Walking stick | Physical prototype |

The team used mounting tape and zip ties to secure the electronics to the walking stick.

Soldered connections were also used to improve connection reliability.

---

## Software Architecture

The software was developed in Python using the gpiozero library.

The system continuously performs the following operations:

1. Trigger ultrasonic sensor A.
2. Measure the echo pulse duration.
3. Calculate the distance to the obstacle.
4. Repeat the process for sensor B.
5. Calculate vibration intensity for each sensor.
6. Select the greater vibration command.
7. Update the vibration motor using PWM.
8. Repeat the process.

The sensor reporting the closest valid obstacle determines the motor's commanded intensity.

---

## Distance Calculation

Ultrasonic sensors determine distance by measuring the time required for a sound pulse to travel to an object and return.

The software uses:

Distance = (Speed of Sound × Echo Duration) / 2

The speed of sound is approximated as:

343 meters per second.

The division by two accounts for the round-trip travel time.

---

## Proximity-Based Vibration

The software uses a detection threshold of 0.30 meters.

Objects outside this range do not activate the vibration motor.

Within the detection range, the PWM duty cycle increases linearly as the object approaches.

The intensity is calculated using:

Intensity = 1 - (Distance / 0.30)

Example commanded PWM values:

| Distance | PWM Duty Cycle |
|----------|----------------|
| 30 cm | 0% |
| 20 cm | 33.3% |
| 15 cm | 50% |
| 10 cm | 66.7% |
| 5 cm | 83.3% |

These values represent commanded PWM duty cycles rather than measured motor vibration strength.

---

## GPIO Configuration

| Component | GPIO Pin |
|-----------|----------|
| Sensor A Trigger | GPIO 4 |
| Sensor A Echo | GPIO 26 |
| Sensor B Trigger | GPIO 17 |
| Sensor B Echo | GPIO 22 |
| Vibration Motor Control | GPIO 14 |

The vibration motor is controlled using PWM through a transistor-based driver circuit.

The Raspberry Pi GPIO pins are not intended to directly supply the current required by the vibration motors.

The HC-SR04 echo signal also requires appropriate voltage-level protection before connecting to a Raspberry Pi GPIO input.

---

## Engineering Challenges

### 1. Motor Power Requirements

One of the primary challenges was supplying sufficient power to the vibration motors without overloading the Raspberry Pi GPIO pins.

The team implemented a transistor-based motor-driving circuit using a breadboard and resistor.

This allowed the GPIO signal to control the motor circuit without directly powering the motors from the GPIO pins.

### 2. Physical Integration

The original design called for a custom 3D-printed walking stick.

However, the printers became unavailable during development.

The team adapted the project to a commercially purchased walking stick and secured the components using mounting tape and zip ties.

### 3. Startup Time

The Raspberry Pi required approximately 90 seconds to become operational after a complete shutdown.

A microcontroller-based design could potentially reduce startup time in future versions.

---

## Project Results

The completed prototype successfully demonstrated:

- Detection of nearby obstacles.
- Distance-based vibration intensity control.
- Integration of two ultrasonic sensors.
- Operation using a Raspberry Pi Zero.
- A functional physical walking-stick prototype.

The total project budget was approximately $90.

The project was completed as an academic prototype rather than a validated mobility device.

---

## Limitations

The prototype has several limitations:

- Approximately 90-second startup time.
- Limited side-facing detection.
- Externally mounted electronics.
- Battery integration constraints.
- No comprehensive validation for real-world mobility use.

Sensor timeouts currently result in no vibration, so an invalid measurement is not distinguished from a clear path.

The prototype is not intended to replace a conventional mobility cane.

---

## Future Improvements

Potential improvements include:

- Replacing the Raspberry Pi with a microcontroller to reduce startup time.
- Adding additional sensors for wider obstacle detection.
- Developing a custom enclosure for the electronics.
- Improving battery integration.
- Improving sensor reliability and fault handling.
- Conducting structured testing of detection accuracy.

---

## Source Code

The Python control program is available here:

[walking_stick.py](walking_stick.py)

---

## Project Documentation

The complete technical project report will be added here.

---

## Team

This project was developed at the University of Houston–Clear Lake by:

- Elijah Hernandez
- Marcos Drabek
- Taran Chan

### Individual Contributions

A detailed breakdown of individual responsibilities will be added after confirming each team member's contributions.

---

## Project Status

Completed academic prototype.

November 2025.
