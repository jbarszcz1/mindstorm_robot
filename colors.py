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


while True:
	##m1.on(sign*speed)
	##m2.on(sign*speed)
	## m3.on(sign*speed)
	## sign = - sign
	## print('Button ' + ('pressed.' if s1.is_pressed else 'not pressed.'))
	#print('Color 1 ' + str(s2.rgb) + ' detected as ' + str(s2.color_name) + '.')
	#print('Color 2 ' + str(s3.rgb) + ' detected as ' + str(s3.color_name) + '.')
	
    
    
    
    red = s2.red
    blue = s2.blue
    green = s2.green
    margin = 100
    color2 = s2.color_name
    if (red<margin and green<margin and blue<margin):
	    color2 = 'Black'
    
    print("lewy czujnik wskazuje: "+color2 )
    print(str(red) + " "+str(green) + " "+str(blue))
    red = s3.red
    blue = s3.blue
    green = s3.green
    margin = 100
    color3 = s3.color_name
	#if (red<margin and green<margin and blue<margin):
	#	color3 = 'Black'
    print("prawy czujnik wskazuje: "+color3 )
    print(str(red) + " "+str(green) + " "+str(blue))
    sleep(2)