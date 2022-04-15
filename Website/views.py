from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html", user=current_user)



@views.route("/dentist")
def dentist():
    return render_template("dentist.html", user=current_user)



@views.route("/patient")
def patient():
    return render_template("patient.html", user=current_user)



@views.route("/receptionist")
def receptionist():
    return render_template("receptionist.html", user=current_user)



@views.route("/patientInfo")  
def patientInfo():
    return render_template("patientInfo.html", user=current_user)


@views.route("/dentistViewAppointment")
def dentistViewAppointment():
    return render_template("dentistViewAppointment.html", user=current_user)


@views.route("dentistViewProcedure")
def dentistViewProcedure():
    return render_template("dentistViewProcedure.html", user=current_user)


@views.route("dentistViewRecord")
def dentistViewRecord():
    return render_template("dentistViewRecord.html", user=current_user)
