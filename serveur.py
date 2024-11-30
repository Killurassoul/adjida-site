import http.server
import socketserver

# Choisis un port (par défaut, 8000)
PORT = 8000

# Dossier où se trouvent les fichiers HTML, CSS et images
DIRECTORY = "C:\\Users\\ideapad Flex5\\Documents\\Adjida"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Démarrer le serveur
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serveur démarré sur http://localhost:{PORT}")
    print("Appuie sur Ctrl+C pour arrêter le serveur.")
    httpd.serve_forever()
