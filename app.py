#!/usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO
import tkinter as tk
from RpiMotorLib import RpiMotorLib

GPIO_pins = (14,15,18)
direction = 20
step = 21

motor = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "A4988")

def sequence():
    """Do a full turn clockwise, then counter clockwise"""
    motor.motor_go(True, "Full" , 200, .0004, False, .02)
    motor.motor_go(False, "Full" , 200, .0004, False, .02)

def turn_left():
    motor.motor_go(True, "Full" , 200, .0004, False, .02)


def turn_right():
    motor.motor_go(False, "Full" , 200, .0004, False, .02)


if __name__ == "__main__":
    root = tk.Tk()

    turn_left = tk.Button(root, text="left", command=turn_left)
    turn_left.grid()

    turn_right = tk.Button(root, text="right", command=turn_right)
    turn_right.grid()

    root.mainloop()