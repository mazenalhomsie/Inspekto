import Communication;
import time;



# Coil address in decimal (0x0800 in hexadecimal is 2048 in decimal)
coil_address = 0x0800

# Coil values

# OK = 0x0001
# NOK = 0x0002

# Communication.write_coil(coil_address, OK)
# time.sleep(5.0)
# Communication.write_coil(coil_address, NOK)
# time.sleep(5.0)
# Communication.write_coil(coil_address, 0x0000)