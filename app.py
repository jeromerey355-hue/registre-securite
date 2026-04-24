from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 SITE OK"

if __name__ == "__main__":
    print("Serveur en démarrage...")
    app.run(debug=True)