from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHttpRequestHandler (SimpleHTTPRequestHandler) :
    def do_GET(self):
        self.path = 'test_server.html'
        return SimpleHTTPRequestHandler.do_GET(self)


def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHttpRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

 

if __name__ == '__main__':
    port = 888
    print("Starting server at port %d" % port)
    server_thread(port)