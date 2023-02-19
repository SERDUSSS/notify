#!/bin/python

import os
import sys
from time import sleep


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

exceptions = [" ","\n","1","2","3","4","5","6","7","8","9","0"]

morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","--.--","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

frequency = 1000



def play_sound(r: str):
    for i in range(len(r)):
        if r[i] == "\n": sleep(1.5)
        elif r[i] == " ": sleep(0.5)
        elif r[i] == ".":
            os.system(f"play -qn -c1 synth {200/1000} sine {frequency}")
        elif r[i] == "-":
            os.system(f"play -qn -c1 synth {500/1000} sine {frequency}")
        else: print(f"{r[i]} : not found")

def play_vibration(r: str):
    for i in range(len(r)):
        sleep(0.1)
        if r[i] == "\n":
            sleep(1.5)
        elif r[i] == " ": sleep(0.5); return 0

        elif r[i] == ".":
            os.system("sudo python ./util.py /sys/class/leds/vibrator/duration 200")
            os.system("sudo python ./util.py /sys/class/leds/vibrator/activate 1")
            return 0
        elif r[i] == "-":
            os.system("sudo python ./util.py /sys/class/leds/vibrator/duration 500")
            os.system("sudo python ./util.py /sys/class/leds/vibrator/activate 1")
            return 0

        else: print(f"{r[i]} : not found"); return 0

def string_to_pseudomorse(string):
    string = string.upper()
    string = list(string)
    for i in range(len(string)):
        if i == len(string) - 1: break
        if string[i] not in letters and string[i] not in exceptions:
            del string[i]


    string = str("".join(string))
    for i in range(len(letters)):
        string = string.replace(letters[i], morse[i])
    return string
