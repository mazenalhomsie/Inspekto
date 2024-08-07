from gpiozero import LED
from time import sleep

# Setup the GPIO pins
relay1 = LED(4)
relay2 = LED(22)
relay3 = LED(6)
relay4 = LED(26)

def Ok():
    relay1.on()
    sleep(5)
    relay1.off()

def NOk():
    relay2.on()
    sleep(5)
    relay2.off()





