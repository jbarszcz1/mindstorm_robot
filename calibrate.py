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


s2.calibrate_white()
s3.calibrate_white()
s2.red_max()
s2.green_max()
s2.blue_max()
s3.red_max()
s3.green_max()
s3.blue_max()
print("success")
