from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException

# Modbus server (GT-226F module) IP and port
modbus_ip = '192.168.100.4'
modbus_port = 502
unit = 6
timeout = 100
retry = 3

# Create a Modbus TCP client
client = ModbusTcpClient(modbus_ip, port=modbus_port, unit= unit)

# Connect to the Modbus server
if client.connect():
    print("Connected to the Modbus Client")
if not client.connect():
    print("Unable to connect to the Modbus server")
    exit(1)

# Function to write a single coil
def write_coil(address, value):
    try:
        result = client.write_register(address, value)
        print(result)
        if result.isError():
            print(f"Error writing coil at address {address}: {result.decode()})")
        else:
            print(f"Successfully wrote {'ON' if value else 'OFF'} to coil at address {address}")
    except ModbusException as e:
        print(f"Modbus exception: {e}")
    except Exception as e:
        print(f"General exception: {e}")




# # Turn on the coil
# write_coil(coil_address, OK)

# Turn off the coil
# write_coil(coil_address, NOK)

# Close the client connection
client.close()
