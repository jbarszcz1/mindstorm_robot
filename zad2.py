#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C,OUTPUT_D

from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor

m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)
m3 = MediumMotor(OUTPUT_D)

## s1 = TouchSensor(INPUT_1)
s2 = ColorSensor(INPUT_2)
s3 = ColorSensor(INPUT_3)



def follow_the_line():

    sign = 1
    print('Color 1 ' + str(s2.rgb) + ' detected as ' + str(s2.color_name) + '.')
    print('Color 2 ' + str(s3.rgb) + ' detected as ' + str(s3.color_name) + '.')
    sleep(0.02)
    red = s2.red
    blue = s2.blue
    green = s2.green
    margin = 80
    color2 = s2.color_name

    if red < margin or green < margin or blue < margin:
        color2 = 'Black'    
    if (str(color2) != 'Black' and str(s3.color_name) != 'Black'):
        speed = 12
        m1.on(sign * speed)
        m2.on(sign * speed)
    if str(color2) == 'Black' and str(s3.color_name) != 'Black':
        speed = 5
        speed1 = 8
        m1.on(sign * speed1)
        m2.on(-sign * speed)
        sleep(0.05)
    if str(color2) != 'Black' and str(s3.color_name) == 'Black':
        speed = 5
        speed1 = 8
        m1.on(-sign * speed)
        m2.on(sign * speed1)
        sleep(0.05)
    if str(color2) == 'Black' and str(s3.color_name) == 'Black':
        speed = 12
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
        sleep(0.5)


def green_found():

        sign = 1
        medium_motor_sign = 1
        medium_motor_speed = 2
        m3.on(medium_motor_sign*medium_motor_speed)
        
        speed = 0
        m1.on(sign * speed)
        m2.on(sign * speed)

        sleep(0.5)

podnoszenie = 0
obrót =0
wyjazd_red1=0
wyjazd_red=0


while True:
    sign = 1
    sleep(0.02)
    if str(s2.color_name) == 'Red' and str(s3.color_name) != 'Red' and wyjazd_red1==0: 
        speed = 5
        speed1 = 8
        m1.on(sign * speed1)
        m2.on(-sign * speed)
        sleep(1)
    elif str(s2.color_name) != 'Red' and str(s3.color_name) == 'Red' and wyjazd_red==0:
        speed = 5
        speed1 = 8
        m1.on(-sign * speed)
        m2.on(sign * speed1)
        sleep(1)
    elif str(s2.color_name) == 'Red' and str(s3.color_name) == 'Red' and podnoszenie==0:
        red_found()
        podnoszenie=1
    elif podnoszenie==1 and obrót==0:
        speed = 15
        m1.on(-sign * speed)
        m2.on(sign * speed)
        sleep(2.2)
        obrót=1
        wyjazd_red=1
        wyjazd_red1=1
    elif str(s2.color_name) == 'Green' and str(s3.color_name) == 'Green':
        green_found()
        break
    elif str(s2.color_name) == 'Green' and str(s3.color_name) != 'Green': 
        speed = 5
        speed1 = 8
        m1.on(sign * speed1)
        m2.on(-sign * speed)
        sleep(1)
    elif str(s2.color_name) != 'Green' and str(s3.color_name) == 'Green':
        speed = 5
        speed1 = 8
        m1.on(-sign * speed)
        m2.on(sign * speed1)
        sleep(1)
    else:
        follow_the_line()
        wyjazd_red=0

