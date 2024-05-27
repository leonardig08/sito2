import http.server
import os
import webbrowser


class SimpleHTTP404RequestHandler(http.server.SimpleHTTPRequestHandler):
    """
    Overrides the default request handler to handle custom 404 pages as 404.html
    (i.e. a 404.html page located in the root). This behavior is seen on:
        GitHub:     https://help.github.com/articles/custom-404-pages/
        FastMail:   https://www.fastmail.com/help/files/website.html

    """
    def do_GET(self):
        path = self.translate_path(self.path)

        # If the path doesn't exist, fake it to be the 404 page.
        if not os.path.exists(path):
            self.path = '404.html'

        # Call the superclass methods to actually serve the page.
        http.server.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    url = "http://localhost:8000/main.html"
    webbrowser.open(url)
    http.server.test(SimpleHTTP404RequestHandler)