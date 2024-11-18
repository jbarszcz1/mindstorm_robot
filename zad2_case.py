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


def odczyt():
    red_left = s2.red
    blue_left = s2.blue
    green_left = s2.green
    red_right = s3.red
    blue_right = s3.blue
    green_right = s3.green
    margin_left = 65
    margin_right = 20
    color_left = s2.color_name
    color_right = s3.color_name

    if red_left < margin_left or green_left < margin_left or blue_left < margin_left:
        color_left = 'Black'

    if red_right < margin_right or green_right < margin_right or blue_right < margin_right:
        color_right = "Black"
    return (color_left, color_right)


def FTL(color_left, color_right):
    sign = 1
    if str(color_left) != 'Black' and str(color_right) != 'Black':
        speed = 10
        m1.on(sign * speed)
        m2.on(sign * speed)
    if str(color_left) == 'Black' and str(color_right) != 'Black':
        speed = 12
        speed1 = 12
        m1.on(sign * speed1)
        m2.on(-sign * speed)
        sleep(0.15)
    if str(color_left) != 'Black' and str(color_right) == 'Black':
        speed = 12
        speed1 = 12
        m1.on(-sign * speed)
        m2.on(sign * speed1)
        sleep(0.15)
    if str(color_left) == 'Black' and str(color_right) == 'Black':
        speed = 10
        m1.on(sign * speed)
        m2.on(sign * speed)


def one_color_found(sign):
    speed = 7
    speed1 = 8
    m1.on(sign * speed)
    m2.on(-sign * speed1)
    sleep(1)


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
    sleep(0.5)
    medium_motor_sign = 1
    medium_motor_speed = 0
    m3.on(medium_motor_sign*medium_motor_speed)
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


def make_turn():
    sign = 1
    speed = 5
    speed1 = 8
    m1.on(-sign * speed)
    m2.on(sign * speed1)
    sleep(2)


one_turn = 0
block_lifted = 0
while True:
    color_left, color_right = odczyt()
    if ((color_left == "Black" or color_left == "White") and (color_right == "Black" or color_right == "White")):
        FTL(color_left, color_right)
    elif (color_left == "Red" and color_right != "Red"):
        one_color_found(sign=1)
    elif (color_left != "Red" and color_right == "Red"):
        one_color_found(sign=-1)
    elif (color_left == "Red" and color_right == "Red" and block_lifted == 0):
        red_found()
        block_lifted = 1
        one_turn = 1
    elif (color_left == 'Black' and color_right == 'Black' and one_turn == 1):
        make_turn()
        one_turn = 0

    elif (color_left == "Green" and color_right != "Green"):
        one_color_found(sign=1)
    elif (color_left != "Green" and color_right == "Green"):
        one_color_found(sign=-1)
    elif (color_left == "Green" and color_right == "Green"):
        green_found()
        break
