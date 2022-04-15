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


@views.route("/setPatientAppoi")
def setPatientAppoi():
    return render_template("setPatientAppoi.html")




@views.route("/patientInfo") 

def patientInfo():
    return render_template("patientInfo.html")


@views.route("dentistViewAppointment")
def dentistViewAppointment():
    return render_template("dentistViewAppointment.html")


@views.route("dentistViewProcedure")
def dentistViewProcedure():
    return render_template("dentistViewProcedure.html")


@views.route("dentistViewRecord")
def dentistViewRecord():
    return render_template("dentistViewRecord.html")
