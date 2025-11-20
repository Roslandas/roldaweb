#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys

# Set the port
PORT = 8000

class SimpleDevServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Serve index.html for all paths except actual files"""
        # If it's a request for an actual file that exists, serve that
        file_path = self.translate_path(self.path)
        if os.path.isfile(file_path):
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        # Otherwise, always serve index.html
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())

def run_server():
    # Change to the directory containing this file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create and start the server
    with socketserver.TCPServer(("", PORT), SimpleDevServer) as httpd:
        print(f"Development server started at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")
            sys.exit(0)

if __name__ == "__main__":
    run_server()