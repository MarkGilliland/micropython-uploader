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

class webrepl():
    def __init__(self, host='192.168.1.25', port=8266, passwd='ktane'):
        self.host = host
        self.port = port
        #Open the socket stuff
        # src_file = '/'

        self.s = socket.socket()

        ai = socket.getaddrinfo(self.host, self.port)
        addr = ai[0][4]

        self.s.connect(addr)
        #s = s.makefile("rwb")
        websocket_helper.client_handshake(self.s)

        self.ws = webrepl_cli.websocket(self.s)

        webrepl_cli.login(self.ws, passwd)
        print("Remote WebREPL version:", webrepl_cli.get_ver(self.ws))

        # Set websocket to send data marked as "binary"
        self.ws.ioctl(9, 2)

    def sendFile(self, filepath):
        #filepath should be a Path obj
        sourceFilepath = str(filepath)
        destinationName = filepath.parts[-1]
        webrepl_cli.put_file(self.ws, sourceFilepath, destinationName)
        print(f'Sent {sourceFilepath}')

                
    def closeConnection(self):
        print("Close")
        self.s.close()

if __name__ == "__main__":
    myWebrepl = webrepl()
    toSend = Path("C:\\Users\\markg\\Desktop\\All Projects\\KTANE Box\\Code\\ktaneBoxCode\\manager-module\\esp32_sys\\blinkLed.py")
    myWebrepl.sendFile
    myWebrepl.closeConnection()





