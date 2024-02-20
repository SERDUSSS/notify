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


for i in range(len(sys.argv)):
    if sys.argv[i] == "-s": sound   = True; morse.frequency = sys.argv[i+1]
    if sys.argv[i] == "-v": vibrate = True
    if sys.argv[i] == "-o": output  = True
    if sys.argv[i] == "-h": human   = True
    if sys.argv[i] == "-d": debug   = True



DoneKeys = {}  # Use a dictionary to keep track of processed keys

while True:
    x = subprocess.run(['termux-notification-list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    x = json.loads(x)

    for notification in x:
        key = notification["key"] + notification["content"]
        package_name = notification["packageName"]
        
        if package_name in AllowList and key not in DoneKeys:
            text = package_name.replace("com", "").replace(".", "") + "\n" + notification["title"] + "\n" + notification["content"]
            text_in_morse = morse.string_to_pseudomorse(text)

            if debug:
                print(f"[!]   {text}")
            if output:
                print(text_in_morse)
            if sound:
                morse.play_sound(text_in_morse)
            if vibrate:
                morse.play_vibration(text_in_morse)
            if human:
                morse.play_human(text)

            # Mark the key as processed
            DoneKeys[key] = True

    # Clean up DoneKeys by removing keys that are no longer in notifications
    DoneKeys = {key: value for key, value in DoneKeys.items() if key in [notification["key"] + notification["content"] for notification in x]}

    t.sleep(5)
