# import sys
import time
from serial.tools import list_ports

i = 0
while 1:
    active_ports = [port for port in list_ports.comports()]
    for port in active_ports:
        print('{}: {} on {}'.format(i, port.description, port.device))
        i += 1
    time.sleep(1)
