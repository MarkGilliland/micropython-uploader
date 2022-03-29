#this uses the webrepl_cli from https://github.com/micropython/webrepl
#I put my own twist on it so it automatically dumps a whole directory

import webrepl_cli
import sys
import os
import struct
try:
    import usocket as socket
except ImportError:
    import socket
import websocket_helper
from pathlib import Path

#Open the socket stuff
host = '192.168.1.25'
port = 8266
src_file = '/'
passwd = 'ktane'

s = socket.socket()

ai = socket.getaddrinfo(host, port)
addr = ai[0][4]

s.connect(addr)
#s = s.makefile("rwb")
websocket_helper.client_handshake(s)

ws = webrepl_cli.websocket(s)

webrepl_cli.login(ws, passwd)
print("Remote WebREPL version:", webrepl_cli.get_ver(ws))

# Set websocket to send data marked as "binary"
ws.ioctl(9, 2)

#

def sendAllInDir(dirToSend):
    files = os.listdir(dirToSend)
    for file in files:
        fileP = Path(f'{dirToSend}\\{file}')
        destinationName = str(fileP).replace('..\\esp32_sys\\', '')
        destinationName = destinationName.replace('\\', '/')
        if fileP.is_dir():#if it is not a file but a subdirectory
##            sendAllInDir(fileP)
            pass
        else:
            webrepl_cli.put_file(ws, str(fileP), destinationName)
            
    
sysDir = '../esp32_sys'
sendAllInDir(sysDir)

##input("Close?")
s.close()



