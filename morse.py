#!/bin/sh

import os
import sys
from time import sleep

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

exceptions = [" ","\n"]

morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","--.--","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def play_sound(r: str):
    if r == "\n": sleep(1.5)
    elif r == " ": sleep(0.5)
    elif r == ".":
        os.system('play -n synth %s sin %s' % (200/1000, frequency))
    elif r == "-":
        os.system('play -n synth %s sin %s' % (500/1000, frequency))

def play_vibration(r: str):
	pass

def string_to_pseudomorse(string):
    for i in range(len(string)):
        if string[i] not in letters and string[i] not in exceptions:
            del string[i]
            i -= 1

    for i in range(len(letters)):
        string = string.replace(letters[i], morse[i])
    return string
