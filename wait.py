# import sys
import time
from serial.tools import list_ports

i = 0
while 1:
    active_ports = [port for port in list_ports.comports()]
    for port in active_ports:
        print(port.description, port.device, port.usb_description(), port.usb_device_path, port.pid, port.vid, port.subsystem)
        i += 1
    time.sleep(1)
