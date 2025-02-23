import sys
import busio
import board
import time
import pigpio
import digitalio
import threading

from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_character_lcd.character_lcd as CharLCD
from adafruit_ads1x15.ads1115 import P0

GAIN = 2 / 3
TENSION = 3.3

TRIG = 16
ECHO = 20
R = 21

RS = digitalio.DigitalInOut(board.D6)
E = digitalio.DigitalInOut(board.D10)
DB7 = digitalio.DigitalInOut(board.D4)
DB6 = digitalio.DigitalInOut(board.D17)
DB5 = digitalio.DigitalInOut(board.D27)
DB4 = digitalio.DigitalInOut(board.D22)

cols = 8
rows = 2
lcd = CharLCD.Character_LCD(RS, E, DB4, DB5, DB6, DB7, cols, rows)

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c, GAIN)
data = AnalogIn(ads, P0)

pi = pigpio.pi()
pi.set_mode(TRIG, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)
pi.set_mode(R, pigpio.OUTPUT)


def alarm():
    while True:
        pi.write(26, 1)  
        pi.write(R, 0)   
        time.sleep(0.9)
        pi.write(26, 0)  
        pi.write(R, 1)   
        time.sleep(0.9)

try:
    while True:

        #Détecter la distance selon la valeur défini par le potentiomètre
        voltage = data.voltage
        if voltage < TENSION / 3:
            valeur = 30.0
        elif voltage < (TENSION / 3) * 2:
            valeur = 70.0
        else:
            valeur = 100.0

        pi.write(TRIG, 1)
        time.sleep(0.00001)
        pi.write(TRIG, 0)

        debut = time.time()
        while pi.read(ECHO) == 0:
            if time.time() - debut > 1:
                break

        echo = time.time()
        while pi.read(ECHO) == 1:
            if time.time() - echo > 1:
                break

        duree = time.time() - echo
        distance = (duree * 34300) / 2
        print("L'alarme est configurée à :" , valeur)

        if distance < valeur:
            
            alarm_thread = threading.Thread(target=alarm)
            alarm_thread.daemon = True 
            alarm_thread.start()

           
           #Condition à appliqué si l'alarme s'active
           
            while True: 
                mdp = "a"
                lcd.message = "Input"
                lcd.cursor_position(0, 1)
                lcd.message = "Password"

                # Prompt for password
                password = input("Veuillez entrer un mot de passe : ")
                #Mauvais mot de passe
                if password != mdp:
                    while True:
                        pi.write(26, 1)  
                        pi.write(R, 0)   
                        time.sleep(0.3)
                        pi.write(26, 0)  
                        pi.write(R, 1)   
                        time.sleep(0.3)
                        lcd.clear()
                        lcd.message = "Police"
                        lcd.cursor_position(0, 1)
                        lcd.message = "Called"
                        
                
                elif password == mdp : 
                #Bon mot de passe
                    pi.write(26, 0)  
                    pi.write(R, 1)
                    lcd.clear()
                    sys.exit()
                

        else:
            print("")

        time.sleep(0.5)

except KeyboardInterrupt:
    lcd.clear()
    sys.exit()
    

finally:
    pi.stop()
   