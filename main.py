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

for i in range(len(sys.argv)):
    if sys.argv[i] == "-s": sound = True; morse.frequency = sys.argv[i+1]
    if sys.argv[i] == "-v": vibrate = True
    if sys.argv[i] == "-o": output = True

while True:
    x = subprocess.run(['termux-notification-list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    if x == "" or x == "\n": system("sudo rm -rf /data/data/com.termux.api/*"); system("termux-api-start")
    x = json.loads(x)

    for i in range(len(x)):
        if x[i]["packageName"] in AllowList:
            text_in_morse = morse.string_to_pseudomorse(x[i]["packageName"].replace("com","").replace(".","") + "\n" + x[i]["title"] + "\n" + x[i]["content"])
            if output: print(text_in_morse)
            if sound: threading.Thread(target=morse.play_sound, args=(text_in_morse,)).start()
            if vibrate: threading.Thread(target=morse.play_vibration, args=(text_in_morse,)).start()

    t.sleep(10)
