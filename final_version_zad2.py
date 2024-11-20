#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor

m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)
m3 = MediumMotor(OUTPUT_D)
s2 = ColorSensor(INPUT_2)
s3 = ColorSensor(INPUT_3)


def follow_the_line():

    sign = 1
    red_left = s2.red
    blue_left = s2.blue
    green_left = s2.green
    red_rigth = s3.red
    blue_right = s3.blue
    green_right = s3.green
    mar_left = 65
    mar_right = 20
    color_left = s2.color_name
    color_right = s3.color_name

    if red_left < mar_left or green_left < mar_left or blue_left < mar_left:
        color_left = 'Black'

    if red_rigth < mar_right or green_right < mar_right or blue_right < mar_right:
        color_right = "Black"

    if str(color_left) != 'Black' and str(color_right) != 'Black':
        speed = 10
        m1.on(sign * speed)
        m2.on(sign * speed)
    if str(color_left) == 'Black' and str(color_right) != 'Black':
        speed = 12
        m1.on(sign * speed)
        m2.on(-sign * speed)
        sleep(0.15)
    if str(color_left) != 'Black' and str(color_right) == 'Black':
        speed = 12
        m1.on(-sign * speed)
        m2.on(sign * speed)
        sleep(0.15)
    if str(color_left) == 'Black' and str(color_right) == 'Black':
        speed = 10
        m1.on(sign * speed)
        m2.on(sign * speed)


def red_found():

    sign = 1
    speed = 10
    m1.on(sign * speed)
    m2.on(sign * speed)
    sleep(0.5)
    medium_motor_sign = -1
    medium_motor_speed = 2
    m3.on(medium_motor_sign*medium_motor_speed)
    speed = 0
    m1.on(sign * speed)
    m2.on(sign * speed)
    m3.on(sign * speed)
    sleep(0.5)
    speed = 15
    m1.on(-sign * speed)
    m2.on(sign * speed)
    sleep(2.4)
    speed = 10
    m1.on(sign * speed)
    m2.on(sign * speed)
    sleep(0.8)


def green_found():

    sign = 1
    medium_motor_sign = 1
    medium_motor_speed = 10
    m3.on(medium_motor_sign*medium_motor_speed)
    speed = 0
    m1.on(sign * speed)
    m2.on(sign * speed)
    sleep(0.5)


def turn_around():
    sleep(0.05)
    speed_forw = 8
    speed_back = 5
    m1.on(sign * speed_forw)
    m2.on(-sign * speed_back)
    sleep(2)


def turn(sign):
    if sign:
        speed_back = 7
        speed_forw = 8
        m1.on(sign * speed_forw)
        m2.on(-sign * speed_back)
        sleep(1)
    else:
        speed_back = 7
        speed_forw = 8
        m1.on(sign * speed_back)
        m2.on(-sign * speed_forw)
        sleep(1)


red_out = 0
turn_once = 0
green_touched = 0


while True:
    color_left = s2.color_name
    color_right = s3.color_name
    sign = 1
    if color_left == 'Red' and color_right != 'Red' and not red_out:
        turn(sign=1)
    elif color_left != 'Red' and color_right == 'Red' and not red_out:
        turn(sign=-1)
    elif color_left == 'Red' and color_right == 'Red' and not red_out:
        red_found()
        red_out = 1
        turn_once = 1
    elif turn_once == 1 and color_left == 'Black' and color_right == 'Black':
        turn_around()
        turn_once = 0
    elif color_left == 'Green' and color_right == 'Green' and green_touched:
        green_found()

        break
    elif color_left == 'Green' and color_right != 'Green' and red_out:
        turn(sign=1)
        green_touched = 1
    elif color_left != 'Green' and color_right == 'Green' and red_out:
        turn(sign=-1)
        green_touched = 1
    else:
        follow_the_line()
