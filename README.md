# Sound localization using power levels

This report presents a method for recording audio using an Arduino, three electret microphones, three LM358 op-amps, and a servo motor with threshold detection, and calculating the sum of vectors in rectangular form to control the servo motor. The microphones are located on a circular surface with 120 degrees from each other and 15 cm distance from the center, and the servo motor is located at the center. The average value of the power levels of the microphones for a 2-second recording is used to define the vectors in polar form, and the vectors are converted to rectangular form and added together to get the result. The result is then converted back to polar form and used to control the servo motor.

Paper link https://scholar.google.com/scholar?oi=bibs&cluster=14530555696231956265&btnI=1&hl=en
