#!/usr/bin/env python
from netmiko import ConnectHandler
import threading
from my_devices import device_list as devices


def remote_cmd(a_device, cmd=""):
    '''
    Execute show version command using Netmiko
    '''
    remote_conn = ConnectHandler(**a_device)
    print
    print '#' * 80
    print remote_conn.send_command(cmd)
    print '#' * 80
    print

def main():
    for a_device in devices:
        my_thread = threading.Thread(target=remote_cmd, args=(a_device, "show arp"))
        my_thread.start()

    main_thread = threading.currentThread()
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            some_thread.join()

if __name__ == "__main__":
    main()
