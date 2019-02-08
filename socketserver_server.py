from socketserver import TCPServer
from socketserver import StreamRequestHandler
from socketserver import ThreadingMixIn
from time import ctime


class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        print('connect form ', self.client_address)
        data = self.rfile.readline().strip().decode()
        print(data)
        self.wfile.write(('[%s] %s' % (ctime(), data)).encode())

class ThreadingTCPSserver(ThreadingMixIn, TCPServer):
    pass


# with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 10001
    ADDRESS = (HOST,PORT)
    with ThreadingTCPSserver(ADDRESS,MyRequestHandler) as server:
        print('waiting for connection')
        server.serve_forever()
