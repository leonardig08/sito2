import http.server
import os
import webbrowser


class SimpleHTTP404RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path):
            self.path = '404.html'
        http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    url = "http://localhost:8000/main.html"
    webbrowser.open(url)
    http.server.test(SimpleHTTP404RequestHandler)