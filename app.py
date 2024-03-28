from sist_sf_2024 import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
