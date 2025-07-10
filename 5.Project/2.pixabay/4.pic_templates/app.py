from flask import Flask, url_for, render_template
import os
from search_routes import search_bp
from admin_routes import admin_bp


app = Flask(__name__)
app.register_blueprint(search_bp, url_prefix="/search")
app.register_blueprint(admin_bp, url_prefix="/admin")

UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)