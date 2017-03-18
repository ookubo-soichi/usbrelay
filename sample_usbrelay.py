#!/usr/bin/python

#cat /etc/udev/rules.d/99-usbrelay.rules 
#SUBSYSTEM=="usb", ATTR{idVendor}=="16c0", ATTR{idProduct}=="05df", MODE="666"

import os, sys, time
import usb.core
import usb.util

def relay_on(dev):
    dev.ctrl_transfer(0x21,0x09,0x0300,0x0000, [0xFF, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

def relay_off(dev):
    dev.ctrl_transfer(0x21,0x09,0x0300,0x0000, [0xFD, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

dev = usb.core.find(idVendor=0x16c0, idProduct=0x5df)
interface = 0

if dev is None:
    print ("device not found")
else:
    print ("device found")
    if dev.is_kernel_driver_active(interface) is True:
        print ("but we need to detach kernel driver")
        dev.detach_kernel_driver(interface)
    dev.set_configuration()

    # To Do Something
    
    print ("release claimed interface")
    usb.util.release_interface(dev, interface)
    print ("now attaching the kernel driver again")
    dev.attach_kernel_driver(interface)
    print ("all done")

