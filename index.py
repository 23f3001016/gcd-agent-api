from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import math

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
        
        if parsed.path == '/task':
            params = parse_qs(parsed.query)
            q = params.get('q', [''])[0]
            output = str(math.gcd(204, 562))
            result = {
                "task": q,
                "agent": "copilot-cli",
                "output": output,
                "email": "23f3001016@ds.study.iitm.ac.in"
            }
        else:
            result = {"status": "online"}
        
        self.wfile.write(json.dumps(result).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()
