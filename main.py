import os
import sys
import time
from serial.tools import list_ports

target_device = 'Arduino Leonardo'
firmware_bin = 'Leonardo-prod-firmware-2012-12-10.hex'


def get_device_port(target_device):
    found_ports = []
    while not found_ports:
        found_ports = [port for port in list_ports.comports()
                       if port.description == target_device]
    if len(found_ports) > 1:
        print('More than one compatible device connected. Exiting.')
        sys.exit()
    # print(len(found_ports))
    return found_ports[0]


def print_device_info(serial_dev):
    print('{} connected at {} with PID {}'.format(
          serial_dev.description, serial_dev.device, serial_dev.pid))


def wait_for_bootloader(target_device, start_pid):
    print('Waiting for bootloader device...')
    current_pid = start_pid
    while (current_pid == start_pid):
        serial_dev = get_device_port(target_device)
        current_pid = serial_dev.pid
        time.sleep(0.25)
    return serial_dev


print('Initial device lookup...')
serial_dev = get_device_port(target_device)
print_device_info(serial_dev)


serial_dev = wait_for_bootloader(target_device, serial_dev.pid)
print('Bootloader connected...')
print_device_info(serial_dev)

cmd = 'avrdude -C ./avrdude.conf -F -p atmega32u4 -c avr109 -b 57600 -P {} -Uflash:w:{}:i'.format(serial_dev.device, firmware_bin)
print(cmd)
# os.system(cmd)
