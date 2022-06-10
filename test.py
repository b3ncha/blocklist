import socket

host = socket.gethostbyaddr("17.0.0.1")

print(host[0])