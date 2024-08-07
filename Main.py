import Communication;
import ip_forwarding;
import mysql_re;
import network_monitoring;



# Eth1 Barcode Scanner Monitoring 
network_monitoring.capture_packets("eth0")  # Capture packets on eth0 interface



# Eth1 Barcode Scanner Monitoring 
# Ancome Ethrenet Frame     
# 1. Send Barcode Scanner Frame to PLC Inspekto 
# 2. Eth2 Receive Frame from PLC Inspekto   OK / NOK
# Database Insert & Load Part into Correcte Magazine    


#at Eth2 Receive Frame make a decision to load part into correct magazine


#todo 
# 1.Show PLC Inspekto Frame
# 2.Show Barcode Scanner Frame

