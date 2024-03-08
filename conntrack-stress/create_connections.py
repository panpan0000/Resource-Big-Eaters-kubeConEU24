import socket
i=0
while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.google.com", 80))
        print(f"Connection {i} established.")
        i=i+1
