from scapy.all import sniff, Ether, IP, TCP
import threading

# Funktionen zum Verarbeiten von Paketen
def process_packet(packet, iface):
    if Ether in packet:
        ether_layer = packet[Ether]
        
        if IP in packet and TCP in packet:
            ip_layer = packet[IP]
            tcp_layer = packet[TCP]
            
            # Beispielentscheidung basierend auf TCP-Daten (hier: Portnummern)
            if tcp_layer.dport == 80 or tcp_layer.sport == 80:
                decision = "OK"
            else:
                decision = "Not OK"
            
            print(f"Interface: {iface}")
            print(f"Source IP: {ip_layer.src}, Destination IP: {ip_layer.dst}")
            print(f"Source Port: {tcp_layer.sport}, Destination Port: {tcp_layer.dport}")
            print(f"Decision: {decision}")
            print("="*50)

# Pakete erfassen
def capture_packets(iface):
    sniff(iface=iface, prn=lambda x: process_packet(x, iface), store=0)

# Hauptfunktion
if __name__ == "__main__":
    # Schnittstellen für Input und Output
    input_iface = "eth0"
    output_iface = "eth1"
    
    # Threads zum gleichzeitigen Erfassen der Pakete auf beiden Schnittstellen
    input_thread = threading.Thread(target=capture_packets, args=(input_iface,))
    output_thread = threading.Thread(target=capture_packets, args=(output_iface,))
    
    # Starten der Threads
    input_thread.start()
    output_thread.start()
    
    # Warten auf die Threads
    input_thread.join()
    output_thread.join()
