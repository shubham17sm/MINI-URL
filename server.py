from main import *

def httpServer():
    try:
        host = ''
        port = 8000
        server = HTTPServer((host, port), webserverHandler)
        print("[SERVER STARTED...]")
        print("Web server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    httpServer()
