import morse
from os import system
import time as t
import subprocess
import json
from allowlist import AllowList

while True:
    x = subprocess.run(['termux-notification-list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    x = json.loads(x)

    for i in range(len(x)):
        if x[i]["packageName"] in AllowList:
            text_in_morse = morse.string_to_pseudomorse(x[i]["packageName"].replace("com","").replace(".","") + "\n" + x[i]["title"] + "\n" + x[i]["content"]

            if sound: Threading.thread(target=morse.play_sound(text_in_morse)
            if vibrate: Threading.thread(target=morse.play_vibration(text_in_morse)

    t.sleep(30)

