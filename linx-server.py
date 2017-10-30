from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import ssl

import ctypes

class LinxDevice():
    def __init__(self):
        self.linxLib = ctypes.cdll.LoadLibrary('/usr/lib/liblinxdevice.so')
        self.linxLib
        self.linxLib.LinxOpen()

    def __del__(self):
        print "Closing linx device"
        self.linxLib.LinxClose()

    def processCommand(self, myByteArray):
        tempBuff = (ctypes.c_ubyte * 256)()
        sendBuff = (ctypes.c_ubyte * len(myByteArray))()
        for index in range(len(myByteArray)):
            sendBuff[index] = myByteArray[index]
        test = self.linxLib.LinxProcessCommand(sendBuff, tempBuff)
        respArryLen = (tempBuff[1] << 8) | (tempBuff[2] & 255)
        trimmedBuf = tempBuff[:respArryLen]
        return trimmedBuf

class S(BaseHTTPRequestHandler):
    linxDevice = LinxDevice()

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        test = bytearray(post_data)
        linxDeviceResp = self.linxDevice.processCommand(test)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/octet-stream')
        self.end_headers()
        self.wfile.write(bytearray(linxDeviceResp))
        
def run(server_class=HTTPServer, handler_class=S, port=4443):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class) 
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile="./server.pem", server_side=True)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()