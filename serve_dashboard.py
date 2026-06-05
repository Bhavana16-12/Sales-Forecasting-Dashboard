import http.server
import socketserver
import webbrowser
import threading
import os
import sys

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow cross-origin requests for local debugging if needed, and set caching headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def open_browser():
    print("Launching web browser to open the dashboard...")
    url = f"http://localhost:{PORT}/dashboard/index.html"
    webbrowser.open(url)

def start_server():
    # Make sure we serve from the root of the project where serve_dashboard.py resides
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    Handler = CustomHTTPRequestHandler
    
    # Allow port reuse to prevent 'Address already in use' errors on quick restarts
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("==========================================================")
        print("          APEX SALES FORECASTING WEB DASHBOARD            ")
        print("==========================================================")
        print(f"Local Server started at: http://localhost:{PORT}/")
        print(f"Direct Dashboard URL: http://localhost:{PORT}/dashboard/index.html")
        print("Press Ctrl+C in this terminal to stop the server.")
        print("==========================================================")
        
        # Open browser in a separate thread after server starts
        threading.Timer(1.0, open_browser).start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server... Goodbye!")
            sys.exit(0)

if __name__ == '__main__':
    start_server()
