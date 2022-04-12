from flask import Flask
from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    # app.config["Secret_Key"] = '_5#y2L"F4Q8znxec]/'
    # app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{DB_NAME}"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SESSION_TYPE"] = "filesystem"
    db.init_app(app)

    from .views import views
    from .auth import auth

    from .models import Patient, Employee

    create_database(app)

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_preffix="/")

    return app


def create_database(app):
    if not path.exists("CSI2132_Project/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")
