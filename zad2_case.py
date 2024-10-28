
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



czujnik_prawy_czerw = 0
czujnik_prawy_ziel = 0
czujnik_lewy_czerw = 0
czujink_lewy_ziel = 0
red_found = 0
green_found = 0


while True:

    
    def switch_case(option):
        if option == 1:
            sign = 1
            print('Color 1 ' + str(s2.rgb) + ' detected as ' + str(s2.color_name) + '.')
            print('Color 2 ' + str(s3.rgb) + ' detected as ' + str(s3.color_name) + '.')
            #sleep(0.02)
            red = s2.red
            blue = s2.blue
            green = s2.green
            red_prawy = s3.red
            blue_prawy = s3.blue
            green_prawy = s3.green
            margin = 80
            margin_prawy = 70
            color2 = s2.color_name
            color3 = s3.color_name
        
            if red < margin or green < margin or blue < margin:
                color2 = 'Black'    
    
            if red_prawy < margin_prawy or green_prawy < margin_prawy or blue_prawy < margin_prawy:
                color3 = "Black"
        elif option == 2:
            return "Wybrano opcję 2"
        elif option == 3:
            return "Wybrano opcję 3"
        else:
            return "Nieznana opcja"
