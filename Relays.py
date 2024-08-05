from gpiozero import LED
from time import sleep

# Setup the GPIO pins
relay1 = LED(4)
relay2 = LED(22)
relay3 = LED(6)
relay4 = LED(26)

def OkRelay():
    relay1.on()
    sleep(5)
    relay1.off()

def NOkRelay():
    relay2.on()
    sleep(5)
    relay2.off()

print("Relay testing!")
while True:
    relay1.on()
    sleep(0.5)
    relay1.off()
    
    relay2.on()
    sleep(5)
    relay2.off()
    
    relay3.on()
    sleep(0.5)
    relay3.off()
    
    relay4.on()
    sleep(0.5)
    relay4.off()
    sleep(0.5)



