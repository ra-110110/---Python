from socket import *
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect(('', 7978))


while True:
    response = s.recv(1024)
    if response:
        data = response.decode('utf-8')
        print(data)
    else:
        continue

