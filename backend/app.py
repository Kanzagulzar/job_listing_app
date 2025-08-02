from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import api
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)
app.register_blueprint(api)

@app.route("/")
def index():
    return "✅ Flask Job API is running"


if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5000)))
