from flask import Flask
from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# from Website import queries

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
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
    if not path.exists("Website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")

        from .models import Patient

        with app.app_context():
            p1 = Patient(id='1234441', username='Jooo', email="joo2o@gmail.com", password='222', firstName="John", lastName="Mashlov", phoneNum=98876555, SSN=124456, role="Patient", insurance="abcInsurance", age=22, gender="Male", houseNum="435/22", street="Kingstons street", province="Ontorio", city="Ottawa")
            db.session.add(p1)
            db.session.commit()
            print("User added")
            print(p1.password)
            print(p1.username)
            print(Patient.query.all())

        # models.populate()



