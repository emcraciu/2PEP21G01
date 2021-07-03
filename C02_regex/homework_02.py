"""Create a class for an object that can retrieve:
 - IP address from each interface on teh system and provide it as a dictionary ex: {'INTERFACE_NAME': 192.168.0.1}
        use command ipconfig (windows) or ifconfig (linux/macOS)
 - IPv4 Route Table as a list of dictionaries. ex: [{'Network Destination': '0.0.0.0', 'Gateway': 192.168.0.1 ...}, {Network...}]
        use command route print (windows) route -n (linux/macOS)"""

