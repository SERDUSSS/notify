import morse
from os import system
import time as t
import subprocess
import json
from allowlist import AllowList
import sys
import threading

sound = False
vibrate = False
output = False
human = False
debug = False

Done = []

for i in range(len(sys.argv)):
    if sys.argv[i] == "-s": sound   = True; morse.frequency = sys.argv[i+1]
    if sys.argv[i] == "-v": vibrate = True
    if sys.argv[i] == "-o": output  = True
    if sys.argv[i] == "-h": human   = True
    if sys.argv[i] == "-d": debug   = True

while True:
    x = subprocess.run(['termux-notification-list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    x = json.loads(x)
    
    for e in range(len(Done)):
        for i in range(len(x)):
            if Done[e] not in x[i]["id"]:
                del Done[e]
                e -= 1
    

    for i in range(len(x)):
        if x[i]["packageName"] in AllowList and x[i]["id"] not in Done:

            text = x[i]["packageName"].replace("com","").replace(".","") + "\n" + x[i]["title"] + "\n" + x[i]["content"]

            text_in_morse = morse.string_to_pseudomorse(text)
            
            if debug:   print(f"[!]   {text}")
            if output:  print(text_in_morse)
            if sound:   morse.play_sound(text_in_morse)
            if vibrate: morse.play_vibration(text_in_morse)
            if human:   morse.play_human(text)
            
            Done += [x[i]["id"]]

    t.sleep(10)
