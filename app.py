from flask import Flask, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_cors import CORS
from db.Models import db
import os

direccion = os.path.abspath(os.getcwd())+"db/modelo.db"
url = 'sqlite:///'+direccion
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tareas4geeks@gmail.com'
app.config['MAIL_PASSWORD'] = '4geeks2019'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db.init_app(app)

CORS(app)
mail = Mail(app)

# RUTAS

def sendmail():
    msg = Message('Hello',
        sender = 'tareas4geeks@gmail.com',
        recipients = ['juanma36@gmail.com']
    )
    msg.subject = "Esto es una prueba"
    msg.html = "<h1>Hola Mundo</h1>"
    mail.send(msg)

    return jsonify({"message":"Email sent"}), 200


@app.route('/test-mail', methods=['GET'])
def home():
    resp = sendmail()

    return jsonify(resp), 200

@app.route('/')
def index():
    return redirect(url_for('/login'))

# Ruta-login
@app.route('/login', methods=['POST'])
def login():
    return jsonify("todo ok")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
