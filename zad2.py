#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor

# Inicjalizacja silników i czujników
m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)
m3 = MediumMotor(OUTPUT_D)

s2 = ColorSensor(INPUT_2)
s3 = ColorSensor(INPUT_3)

# Definicje prędkości
LINE_FOLLOW_SPEED = 10
TURN_SPEED = 12
RED_FOUND_SPEED = 10
GREEN_FOUND_SPEED = 10

def follow_the_line():
    """Funkcja do śledzenia linii."""


    color_left = detect_color(s2)
    color_right = detect_color(s3)

    if color_left == 'Black' and color_right != 'Black':
        turn(TURN_SPEED, -TURN_SPEED)
    elif color_left != 'Black' and color_right == 'Black':
        turn(-TURN_SPEED, TURN_SPEED)
    else:
        move_forward(LINE_FOLLOW_SPEED)

def detect_color(sensor):
    """Detekcja koloru na podstawie wartości RGB."""
    red = sensor.red
    green = sensor.green
    blue = sensor.blue

    if red < 45 and green < 45 and blue < 45:  # Czarny
        return 'Black'
    elif green > 60 and red < 50 and blue < 50:  # Zielony
        return 'Green'
    elif red > 60 and green < 50 and blue < 50:  # Czerwony
        return 'Red'
    elif red > 60 and green > 60 and blue > 60:  # Biały
        return 'White'
    else:
        return str(sensor.color_name)

def move_forward(speed):
    """Porusza robot do przodu z określoną prędkością."""
    m1.on(speed)
    m2.on(speed)

def turn(speed_left, speed_right):
    """Obrót robota."""
    m1.on(speed_left)
    m2.on(speed_right)
    sleep(0.15)  # czas obrotu

def red_found():
    """Akcje do wykonania po znalezieniu czerwonego koloru."""
    move_forward(RED_FOUND_SPEED)
    sleep(0.5)
    m3.on(-2)  # ruch silnika medium
    stop_motors()

def green_found():
    """Akcje do wykonania po znalezieniu zielonego koloru."""
    m3.on(GREEN_FOUND_SPEED)
    stop_motors()

def stop_motors():
    """Zatrzymuje wszystkie silniki."""
    m1.off()
    m2.off()

while True:
    color_left = detect_color(s2)
    color_right = detect_color(s3)

    if color_left == 'Red' and color_right != 'Red':
        turn(-7, 8)
        sleep(1)
    elif color_left != 'Red' and color_right == 'Red':
        turn(8, -7)
        sleep(1)
    elif color_left == 'Red' and color_right == 'Red':
        red_found()
    elif color_left == 'Green' and color_right == 'Green':
        green_found()
        break
    else:
        follow_the_line()
