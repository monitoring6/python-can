#!/usr/bin/env python

from __future__ import print_function
import time
import can

print("Robotell Send!!!")

bus = can.interface.Bus(bustype='robotell', channel='COM5@115200', bitrate=9600)

serialNumber = bus.get_serial_number(None)     
if serialNumber is not None:
    print(f"{bus.channel_info}")

#bus.set_serial_rate(115200) 
#bus.set_bitrate(115200)

msg = can.Message(arbitration_id=0xC0FFEE, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True)
try:
    while True:
        bus.send(msg)
        print(f"Message sent {msg.data}")
        time.sleep(1)
except can.CanError:
    print("Message NOT sent")

