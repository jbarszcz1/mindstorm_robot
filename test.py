#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C

from ev3dev2.sensor import INPUT_1, INPUT_2,INPUT_3
from ev3dev2.sensor.lego import TouchSensor, ColorSensor

m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)
## m3 = MediumMotor(OUTPUT_C)

## s1 = TouchSensor(INPUT_1)
s2 = ColorSensor(INPUT_2)
s3 = ColorSensor(INPUT_3)

sign = 1
speed = 25


while True:
    print('Color 1 ' + str(s2.rgb) + ' detected as ' + str(s2.color_name) + '.')
    print('Color 2 ' + str(s3.rgb) + ' detected as ' + str(s3.color_name) + '.')
    sleep(0.1)
    if(str(s2.color_name) != 'Black' and str(s3.color_name) != 'Black'):
		
        speed = 10
        m1.on(sign*speed)
        m2.on(sign*speed)
    if(str(s2.color_name) == 'Black' and str(s3.color_name) != 'Black'):
    
        speed = 5
        speed1= 5
        m1.on(sign*speed1)
        m2.on(-sign*speed)
        sleep(0.3)
    if(str(s2.color_name) != 'Black' and str(s3.color_name) == 'Black'):
    
        speed = 5
        speed1= 5
        m1.on(-sign*speed)
        m2.on(sign*speed1)
        sleep(0.3)
        
    if(str(s2.color_name) == 'Black' and str(s3.color_name) == 'Black'):
    
        speed = 10
        m1.on(sign*speed)
        m2.on(sign*speed)
        