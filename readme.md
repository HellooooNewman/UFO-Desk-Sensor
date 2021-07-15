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

## Dev testing
SSH for Raspberry Pi
*note* You'll need to find your own pi's ip address
```
ssh pi@192.168.50.78
ssh pi@192.168.0.172
```

Turn on Program
```
cd Documents/UFO-Desk-Sensor
sudo python3 dtc3.py
```

Light Test
```
cd Documents/rpi_ws281x/python/examples
sudo python3 strandtest.py -c
```

## Final Thoughts
I could have made this cheaper and easier with an Ardunio and a 
Ultrasonic Distance Sensor, but I wasn't sure on how loud it would be and I had already bought a Raspberry Pi.
