from main import *
import argparse

def httpServer(host, port):
    try:
        if connection_status == True:
            server = HTTPServer((host, port), webserverHandler)
            print("[SERVER STARTED]Web server running on port %s" % port)
            server.serve_forever()
        else:
            raise(NameError)
    except NameError:
        print("Can't start the server due to database connection failed")
    except KeyboardInterrupt:
        print(" ^C entered stopping web server...")
        server.socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Host address", default="")
    parser.add_argument("--port", help="port number", type=int, default=8000)
    args = parser.parse_args()
    httpServer(args.host, args.port)
