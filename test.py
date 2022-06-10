# Quelle: https://stackoverflow.com/questions/2575760/python-lookup-hostname-from-ip-with-1-second-timeout
# 
import socket

host = socket.gethostbyaddr("17.0.0.2")

print(host[0])