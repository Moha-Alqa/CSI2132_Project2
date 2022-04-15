from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/dentist")
def dentist():
    return render_template("dentist.html")


@views.route("/patient")
def patient():
    return render_template("patient.html")


@views.route("/receptionist")
def receptionist():
    return render_template("receptionist.html")


@views.route("/patientInfo")  # syntax error
def patientInfo():
    return render_template("patientInfo.html")


@views.route("/receptionistEditInfo")
def receptionistEditInfo():
    return render_template("receptionistEditInfo.html")

