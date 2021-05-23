from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["ENV"] = "DEVELOPMENT"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "DEVELOPMENT"

db = SQLAlchemy(app)
Migrate(app,db)

@app.route("/")
def index():
    return "hello kitty" 
@app.route("/profile")
def profile():
    return render_template("profile.html")
@app.route("/search_plugin")
def search_plugin():
    return render_template("search_plugin.html")
