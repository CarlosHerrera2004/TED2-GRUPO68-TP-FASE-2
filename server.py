import http.server
import socketserver

PORT = 8000

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_POST(self):
        if self.path == '/save-mind':
            try:
                length = int(self.headers.get('Content-Length', 0))
                data = self.rfile.read(length)
                with open('targets/targets.mind', 'wb') as f:
                    f.write(data)
                with open('targets/target.mind', 'wb') as f:
                    f.write(data)
                with open('targets.mind', 'wb') as f:
                    f.write(data)
                with open('target.mind', 'wb') as f:
                    f.write(data)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'OK')
                print(f"[OK] Archivo targets.mind actualizado exitosamente ({len(data)} bytes)")
                return
            except Exception as e:
                self.send_error(500, str(e))
                return
        self.send_error(404)

    def guess_type(self, path):
        if path.endswith('.mind'):
            return 'application/octet-stream'
        if path.endswith('.glb'):
            return 'model/gltf-binary'
        return super().guess_type(path)

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
        httpd.serve_forever()
