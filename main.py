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

Done = []

for i in range(len(sys.argv)):
    if sys.argv[i] == "-s": sound = True; morse.frequency = sys.argv[i+1]
    if sys.argv[i] == "-v": vibrate = True
    if sys.argv[i] == "-o": output = True

while True:
    x = subprocess.run(['termux-notification-list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    if x == "" or x == "\n": system("sudo rm -rf /data/data/com.termux.api/*"); system("termux-api-start")
    x = json.loads(x)
    
    for e in range(len(Done)):
        for i in range(len(x)):
            if Done[e] not in x[i]["id"]:
                del Done[e]
                e -= 1
    

    for i in range(len(x)):
        if x[i]["packageName"] in AllowList and x[i]["id"] not in Done:
            
            text_in_morse = morse.string_to_pseudomorse(x[i]["packageName"].replace("com","").replace(".","") + "\n" + x[i]["title"] + "\n" + x[i]["content"])
            
            if output: print(text_in_morse)
            if sound: morse.play_sound(text_in_morse)
            if vibrate: morse.play_vibration(text_in_morse)
            
            Done += [x[i]["id"]]

    t.sleep(10)
