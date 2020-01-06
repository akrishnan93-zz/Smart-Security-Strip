import webiopi
from webiopi.clients import *
from time import sleep

gpio = webiopi.GPIO
PIN=4

def setup():
    gpio.setFunction(PIN, gpio.OUT)

def destroy():
    print("destroy called")
    gpio.digitalWrite(PIN, gpio.HIGH)
    exit()

@webiopi.macro
def blink(userInput):
    count = 0
    while (count < int(userInput) * 2):
        state = gpio.digitalRead(PIN)
        gpio.digitalWriter(PIN, not state)
        print("in blink")
        webiopi.sleep(1)
        count = count + 1

@webpio.macro
def SOS():
    print("in SOS")
    count = 0
    while (count < 8):
        state = gpio.digitalRead(PIN)
        gpio.digitalWrite(PIN, not state)
        webipio.sleep(0.3)
        count = count + 1

@webiopi.macro
def setCount(count):
    global COUNT
    COUNT = int(count)
    print("in count function")
    print(count)
