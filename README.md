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

<h3>Ultrasonic Proximity Sensor (HC-SR04)</h3>
<p>This module detects the presence of an individual at a distance. In our project, the distance is adjustable up to a maximum of 1.2 meters.</p>


![s-l400](https://github.com/user-attachments/assets/65a9f341-c6a4-4467-b544-686edc4465db)

<h3>RGB LED</h3>
<p>The RGB LED activates whenever an individual passes in front of the sensor, blinking until the correct password is entered. If an incorrect password is entered, the RGB LED will blink more rapidly.</p>


![1 1](https://github.com/user-attachments/assets/ace3f1d0-165e-4b12-878f-90d75152b5a8)

<h3>LCD Screen</h3>
<p>The LCD screen displays instructions for the user, such as prompting for password entry. If the password is incorrect, it shows a message indicating that the police have been alerted.</p>

<h3>Buzzer</h3>
<p>The buzzer activates as soon as an individual is detected. It will turn off if the correct password is entered; however, if the password is incorrect, it will emit a sound at a faster rate.</p>

<h3>2 Potentiometers</h3>
<ol>
    <li> potentiometer 1 adjusts the contrast of the LCD screen to enhance visibility.</li>
    <li> potentiometer 2 allows for the adjustment of the detection distance of the ultrasonic proximity sensor.</li>
</ol>

<h3>ADS1115 Module</h3>
<p>This module enables the connection of the potentiometer to ensure it functions properly.</p>
