# UFO Standing Desk Sensor

## Requirements
- Raspberry Pi
- BreadBoard
- 5V power supply
- Camera
- 3D printer
- Printed 6x6 Aruco marker (https://chev.me/arucogen/)
- Standing desk
- Hook to hold it to the ceiling
- NeoPixel ring lights

## Install
 Make sure you have python3 and pip3 installed

`pip3 install opencv-python opencv-contrib-python numpy imutils`

## Hardware Setup
Coming soon!

## Desk Setup
- Place ufo above desk
- Place Aruco marker behind monitor
- Run `python3 dtc3.py`

## Results
Now when you move your desk up or down the lights on the ufo will light up

## Future Improvements
- Light color changes depending on if it's moving up or down
- Little speaker on it?
- Rotating parts?

## Final Thoughts
I could have made this cheaper and easier with an Ardunio and a 
Ultrasonic Distance Sensor, but I wasn't sure on how loud it would be and I had already bought a Raspberry Pi.