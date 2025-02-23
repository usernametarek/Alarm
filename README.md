# Alarm-System-with-Raspberry-PI-5
Easy alarm system to make with a Raspberry PI 5 and it's components
<h2>Project Overview</h2>
<p>Our project aims to recreate a smart alarm system. When an individual passes in front of the distance sensor at a predefined distance, a sound alarm will trigger, and a red LED light will blink. An LCD screen will then prompt the individual to enter a password.</p>
<p>Two scenarios can occur:</p>
<ol>
    <li>If the individual enters the correct password, the system will return to normal.</li>
    <li>If the individual enters the incorrect password, the sound and LED will activate more rapidly, and the LCD screen will display an alert message indicating that the police have been notified.</li>
</ol>
<h2>Components needed</h2>
<p>To build this project, you will need the following components as showed in the picture.</p>

![ajnrbghaebaehkn](https://github.com/user-attachments/assets/c6bc99f2-ba98-4c8c-bb3b-8321f6f2867e)


<h3>Ultrasonic Proximity Sensor (HC-SR04)</h3>
<p>This module detects the presence of an individual at a distance. In our project, the distance is adjustable up to a maximum of 1.2 meters.</p>


![s-l400](https://github.com/user-attachments/assets/65a9f341-c6a4-4467-b544-686edc4465db)

<h3>RGB LED</h3>
<p>The RGB LED activates whenever an individual passes in front of the sensor, blinking until the correct password is entered. If an incorrect password is entered, the RGB LED will blink more rapidly.</p>


![1 1](https://github.com/user-attachments/assets/ace3f1d0-165e-4b12-878f-90d75152b5a8)

<h3>LCD Screen 0802</h3>
<p>The LCD screen displays instructions for the user, such as prompting for password entry. If the password is incorrect, it shows a message indicating that the police have been alerted.</p>


![2846-LCD802A_main-500x500](https://github.com/user-attachments/assets/22aedb35-1ed6-4dfd-961d-0bc2fe02153c)


<h3>Buzzer</h3>
<p>The buzzer activates as soon as an individual is detected. It will turn off if the correct password is entered; however, if the password is incorrect, it will emit a sound at a faster rate.</p>


![buzzer](https://github.com/user-attachments/assets/465a105d-aee0-4e99-bb66-e47a7a844e45)


<h3>2 Potentiometers</h3>
<ol>
    <li> potentiometer 1 adjusts the contrast of the LCD screen to enhance visibility.</li>
    <li> potentiometer 2 allows for the adjustment of the detection distance of the ultrasonic proximity sensor.</li>

![pot](https://github.com/user-attachments/assets/e763ee4e-8ff6-4a06-9718-1060bee426d4)
</ol>

<h3>ADS1115 Module</h3>
<p>This module enables the connection of the potentiometer to ensure it functions properly.</p>

![319104169_ads1115-16-bit-adc-module_x](https://github.com/user-attachments/assets/5b7e0e69-f055-4a7e-8e17-012d0f0581f3)

<h3>prototyping board</h3>
<p>used to facilitate multiple connections</p>

![breadboard](https://github.com/user-attachments/assets/9dc16f0e-9247-41e1-8cea-2c3acc1eadb1)


<h2>Setting up</h2>
<h3>GPIO Pin Configuration</h3>

1. **Ultrasonic Sensor (HC-SR04)**
   - TRIG: GPIO 16 
   - ECHO: GPIO 20
   - VCC : 5V
   - GNG : GROUND

2. **Buzzer**
   - S: GPIO 26 
   - V: 3.3V
   - G: Ground

3. **LED**
   - R: GPIO 21 
   - V: 3.3V
   - G: Ground

4. **LCD Display**
   - RS: GPIO 6 (D6)
   - E: GPIO 10 (D10)
   - DB4: GPIO 22 (D22)
   - DB5: GPIO 27 (D27)
   - DB6: GPIO 17 (D17)
   - DB7: GPIO 4 (D4)
   - RW: Ground
   - VSS: Ground
   - VDD: 5V
   - V0: Connect to the second potentiometer S pin
  
    ![lcd_gpio](https://github.com/user-attachments/assets/e38ac850-0ef9-4add-9664-122225a9e3f3)


5. **ADS1115 Module**
     - SDA: GPIO 2 
     - SCL: GPIO 3
     - VDD: 3.3V
     - GND: Ground
     - A0: Connect to the first potentiometer S pin

6. **Potentiometer 1**
   - S: Connect to the ADS1115's analog input (A0).
   - V: 3.3V
   - G: Ground

7. **Potentiometer 2**
   - S: Connect to the LCD Display V0 Pin
   - V: 5V
   - G: Ground
  
<h3>Software Requierements</h3>
<ol>
    <li>Python 3</li>
</ol>
    
<h4>Required libraries</h4>
<ol>
    <li><strong>sys</strong>: Provides functions and variables for manipulating the runtime environment.</li>
    <li><strong>busio</strong>: Used for I2C communication.</li>
    <li><strong>board</strong>: Defines pin names for the LCD screen.</li>
    <li><strong>time</strong>: Provides functions for manipulating time.</li>
    <li><strong>pigpio</strong>: Used to control GPIO on a Raspberry Pi.</li>
    <li><strong>digitalio</strong>: Allows working with digital pins (reading and writing).</li>
    <li><strong>threading</strong>: Provides tools for creating and managing threads.</li>
    <li><strong>adafruit_ads1x15</strong>: Library for interacting with analog-to-digital converters.</li>
    <li><strong>ADS1115</strong>: Specific class for the ADS1115 model.</li>
    <li><strong>AnalogIn</strong>: Used to read analog inputs.</li>
    <li><strong>adafruit_character_lcd</strong>: Library for controlling a character LCD.</li>
</ol>





