#!/usr/bin/env python

from __future__ import print_function
import time
import can

print("Robotell Receive!")

bus = can.interface.Bus(bustype='robotell', channel='COM6@115200', bitrate=9600)

serialNumber = bus.get_serial_number(None)     
if serialNumber is not None:
    print(f"Robotell serialNUmber: {serialNumber}")

#bus.set_serial_rate(115200) 
#bus.set_bitrate(115200)

try:
    while True:
        msg = bus.recv(1)
        if msg is not None:
            print(msg)
except KeyboardInterrupt:
    pass