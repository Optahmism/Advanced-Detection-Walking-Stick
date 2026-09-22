"""
Advanced Detection Walking Stick

Dual ultrasonic sensor obstacle detection with
PWM-controlled vibration feedback.

Hardware:
- Raspberry Pi Zero
- Two HC-SR04 ultrasonic sensors
- Vibration motor and transistor driver

Academic team project, University of Houston-Clear Lake
November 2025
"""

from gpiozero import InputDevice, OutputDevice, PWMOutputDevice
from time import sleep, time


# ----------------------------------
# GPIO CONFIGURATION
# ----------------------------------

# Ultrasonic Sensor A
trigA = OutputDevice(4)
echoA = InputDevice(26)

# Ultrasonic Sensor B
trigB = OutputDevice(17)
echoB = InputDevice(22)

# Vibration motor
motor = PWMOutputDevice(14)

# Allow sensors to initialize
sleep(2)


# ----------------------------------
# ULTRASONIC SENSOR FUNCTION
# ----------------------------------

def get_pulse_time(trig, echo, timeout=0.02):
    """
    Measure the echo pulse duration from
    an ultrasonic sensor.

    Returns:
        Pulse duration in seconds,
        or None if a timeout occurs.
    """

    trig.on()
    sleep(0.00001)
    trig.off()

    start_time = time()

    # Wait for echo signal to go HIGH
    while not echo.is_active:
        if time() - start_time > timeout:
            return None

    pulse_start = time()

    # Wait for echo signal to go LOW
    while echo.is_active:
        if time() - pulse_start > timeout:
            return None

    pulse_end = time()

    return pulse_end - pulse_start


# ----------------------------------
# DISTANCE CALCULATION
# ----------------------------------

def calculate_distance(duration):
    """
    Calculate distance using echo duration
    and the speed of sound.

    Returns distance in meters.
    """

    if duration is None:
        return None

    speed_of_sound = 343

    return (speed_of_sound * duration) / 2


# ----------------------------------
# VIBRATION CONTROL
# ----------------------------------

def vibration_from_distance(dist_m):
    """
    Convert distance into PWM intensity.

    Objects 30 cm or farther produce
    no vibration.

    Closer objects produce stronger
    vibration commands.
    """

    max_distance = 0.30

    if dist_m is None or dist_m >= max_distance:
        return 0.0

    intensity = 1 - (dist_m / max_distance)

    return intensity


# ----------------------------------
# MAIN CONTROL LOOP
# ----------------------------------

while True:

    # Read ultrasonic sensor A
    pulseA = get_pulse_time(trigA, echoA)
    distA = calculate_distance(pulseA)

    # Read ultrasonic sensor B
    pulseB = get_pulse_time(trigB, echoB)
    distB = calculate_distance(pulseB)

    # Display measurements
    print(f"A: {distA} m | B: {distB} m")

    # Calculate vibration intensity
    intensityA = vibration_from_distance(distA)
    intensityB = vibration_from_distance(distB)

    # Prioritize the closest detected object
    motor.value = max(intensityA, intensityB)

    # Delay before next measurement
    sleep(0.1)
