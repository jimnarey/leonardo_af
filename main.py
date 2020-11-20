import sys
from serial.tools import list_ports

compat_devices = ['Arduino Leonardo']

active_ports = [port for port in list_ports.comports()
                if port.description in compat_devices]

if len(active_ports) > 1:
    print('More than one compatible device connected. Exiting...')
    sys.exit()

port = active_ports[0]

print('{} connected at {}'.format(port.description, port.device))
