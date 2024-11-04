#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor

# Inicjalizacja silników
m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)
m3 = MediumMotor(OUTPUT_D)

# Inicjalizacja czujników kolorów
s2 = ColorSensor(INPUT_2)
s3 = ColorSensor(INPUT_3)

def detect_color(sensor):
    """Funkcja do detekcji koloru na podstawie wartości RGB."""
    red = sensor.red
    green = sensor.green
    blue = sensor.blue

    # Przedziały kolorów
    if 40 < green < 255 and red < 50 and blue < 50:  # Zielony
        return 'Green'
    elif 50 < red < 255 and green < 50 and blue < 50:  # Czerwony
        return 'Red'
    elif 50 < blue < 255 and red < 50 and green < 50:  # Niebieski
        return 'Blue'
    elif red < 20 and green < 20 and blue < 20:  # Czarny
        return 'Black'
    elif red > 100 and green > 100 and blue > 100:  # Biały
        return 'White'
    else:
        return "Unknown"

# Pętla główna
while True:
    # Odczyty kolorów z czujników
    color_left = detect_color(s2)
    color_right = detect_color(s3)

    # Wyświetlanie wyników
    print("Left color detected: {}".format(color_left))
    print("Right color detected: {}".format(color_right))
    

    sleep(1)  # Przerwa między odczytami
