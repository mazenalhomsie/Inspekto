from time import sleep
from gpiozero import LED;

print("Relay testing!")

relay1 = LED(4)
relay2 = LED(22)
relay3 = LED(6)
relay4 = LED(26)


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