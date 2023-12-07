# Proxy-Server-Rotation

The code is a Python program that creates a packet sniffer using Scapy and tkinter. The program allows the user to monitor network traffic for a specific subdomain and displays the source and destination IP addresses of each packet in a tree view widget.
 The program uses threading to run the packet sniffing function in the background and collections module to store the IP addresses in a dictionary. The user can start and stop packet sniffing using two buttons provided in the GUI.
In brief, the program creates a GUI using tkinter, consisting of an entry field for the subdomain, a tree view widget to display the IP addresses, and two buttons for starting and stopping packet sniffing. The packet sniffing function captures network packets using Scapy's sniff() function and extracts the source and destination IP addresses using the find_ips() function. 

The program updates the tree view widget with the new IP addresses and uses a default dictionary called scr_ip_dict to avoid duplication. The user can start and stop packet sniffing using the buttons provided in the GUI.
