
import network_monitoring
#make observer pattern for the barcode scanner and plc inspekto



class EthernetObserver:
    def __init__(self, name):
        self.name = name

    def update(self, packet):
        # Process the received packet
        print(f"{self.name} received packet: {packet}")

# Create instances of observers
barcode_observer = EthernetObserver("Barcode Scanner")
# plc_observer = EthernetObserver("PLC Inspekto")

# Register the observers to the network monitoring module
network_monitoring.register_observer(barcode_observer)
# network_monitoring.register_observer(plc_observer)

