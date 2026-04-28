from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import string

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Default settings
        length = 10
        use_upper = True
        use_lower = True
        use_numbers = True
        use_specials = True

        
        try:
            # split path and query manually
            parts = self.path.lstrip('/').split('?')
            if parts[0].isdigit():
                length = int(parts[0])

            if len(parts) > 1:
                query = parts[1].split('&')
                for q in query:
                    key_value = q.split('=')
                    if len(key_value) == 2:
                        key, value = key_value
                        value = value == '1'
                        if key == 'upper':
                            use_upper = value
                        elif key == 'lower':
                            use_lower = value
                        elif key == 'numbers':
                            use_numbers = value
                        elif key == 'specials':
                            use_specials = value
        except:
            pass

        all_chars = ''
        if use_upper:
            all_chars += string.ascii_uppercase
        if use_lower:
            all_chars += string.ascii_lowercase
        if use_numbers:
            all_chars += string.digits
        if use_specials:
            all_chars += "!@#$%^&*?"

        if not all_chars:
            all_chars = string.ascii_letters + string.digits + "!@#$%^&*?"

        password = "".join(random.choice(all_chars) for _ in range(length))

        
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(password.encode())

# start server
server = HTTPServer(("localhost", 8000), MyServer)
print("Server started at http://localhost:8000")
server.serve_forever()
