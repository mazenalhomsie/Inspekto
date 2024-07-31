from scapy.all import sniff, sendp, IP, Ether

# Define the IP address to monitor and the output interface
MONITOR_IP = "192.168.100.10"
OUTPUT_INTERFACE = "eth2"

def packet_callback(packet):
    # Check if the packet is destined for the monitor IP
    if IP in packet and packet[IP].dst == MONITOR_IP:
        # Forward the packet to the output interface
        sendp(Ether()/packet[IP], iface=OUTPUT_INTERFACE)
        print(f"Forwarded packet to {OUTPUT_INTERFACE}: {packet.summary()}")

# Start sniffing on all interfaces for packets destined to the monitor IP
sniff(filter=f"dst host {MONITOR_IP}", prn=packet_callback)
