import http.server
import socketserver
import webbrowser

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# 1. Enable address reuse to prevent "Address already in use" errors
class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

httpd = None

try:
    # 2. Use the new ReusableTCPServer
    httpd = ReusableTCPServer(("", PORT), Handler)
    print(f"Serving at http://localhost:{PORT}")
    
    webbrowser.open(f'http://localhost:{PORT}')
    
    httpd.serve_forever()
    
except KeyboardInterrupt:
    # This catches the Stop button press in Pythonista
    print("\nStop button pressed.")
    
finally:
    # 3. This block ALWAYS runs, guaranteeing the port is freed
    if httpd:
        httpd.server_close()
        print(f"Server completely shut down and Port {PORT} freed.")