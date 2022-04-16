from crypt import methods
from curses.ascii import EM
from email import message
import email
from Website import views
from . import db
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    redirect,
)

from .models import Patient, Employee, Appointment

from Website import models
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from flask_login import LoginManager


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        role = request.form.get("role")

        if role == "Patient":
            user = Patient.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    return redirect(url_for("views.patient"))
                else:
                    flash("Incorrect password, try again")
            else:
                flash("User does not exist")
        elif role == "Dentist" or role == "Receptionist":
            user = Employee.query.filter_by(username=username).first()

            if user:
                if check_password_hash(user.password, password) and role == "Dentist":
                    login_user(user, remember=True)
                    flash("Logged in successfully")
                    return redirect(url_for("views.dentist"))
                elif (
                    check_password_hash(user.password, password)
                    and role == "Receptionist"
                ):
                    login_user(user, remember=True)
                    flash("Logged in successfully")
                    return redirect(url_for("views.receptionist"))
                else:
                    flash("Incorrect password, try again")
            flash("User does not exist")
        else:
            flash("Input your username and password")

    return render_template("login.html", user=current_user)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    message = None
    data = request.form
    print(data)
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        phoneNum = request.form.get("phoneNum")
        SSN = request.form.get("SSN")
        insurance = request.form.get("insurance")
        salary = request.form.get("salary")
        role = request.form.get("role")
        gender = request.form.get("gender")
        age = request.form.get("age")
        houseNum = request.form.get("houseNum")
        street = request.form.get("street")
        province = request.form.get("province")
        city = request.form.get("city")

        if role == "Patient":
            user = Patient.query.filter_by(email=email).first()
        else:
            user = Employee.query.filter_by(email=email).first()

        if user:
            message = "Email already exists"

        elif len(username) <= 2:
            message = "Username must be greater than 1 characters"
        elif len(firstName) < 3 and not (firstName.isalpha()):
            message = "First Name must be greater than 3 characters and only includes characters"
        elif len(lastName) < 3 and not (lastName.isalpha()):
            message = "Last Name must be greater than 3 characters and only includes characters"
        elif (len(email) < 2) and not ("@" in email):
            message = "Email must be greater than 2 characters and includes @"
        elif password1 != password2:
            message = "Passwords must match"
        elif len(phoneNum) < 2 or not (phoneNum.isnumeric()):
            message = (
                "Phone number must be greater than 2 numbers and only includes numbers"
            )
        elif len(SSN) < 2 or not (SSN.isnumeric()):
            message = "SSN must be greater than 2 numbers and only includes numbers"
        elif len(insurance) < 2 or not (insurance.isalnum()):
            message = "Insurance name must be greater than 2 characters and includes numbers or characters"
        elif len(houseNum) < 2:
            message = "House number name must be greater than 2 characters"
        elif len(street) < 2:
            message = "Streat must be greater than 2 characters"
        elif len(city) < 2 or not (city.isalpha()):
            message = "City name must be greater than 2 characters and includes only characters"
        elif len(province) < 2 or not (province.isalpha()):
            message = "Province name must be greater than 2 characters and includes only characters"
        else:
            if role == "Patient":
                new_user = Patient(
                    username=username,
                    email=email,
                    firstName=firstName,
                    lastName=lastName,
                    role=role,
                    password=generate_password_hash(password1, method="sha256"),
                    phoneNum=phoneNum,
                    gender=gender,
                    SSN=SSN,
                    insurance=insurance,
                    age=age,
                    houseNum=houseNum,
                    street=street,
                    city=city,
                    province=province,
                )
                db.session.add(new_user)
                db.session.commit()
                flash("Account Created Successfully")
                return redirect(url_for("auth.login"))
            else:
                if len(salary) < 1 or not (salary.isnumeric()):
                    flash(
                        "Salary must be greater than 1 number and only includes numbers"
                    )
                else:
                    new_user = Employee(
                        username=username,
                        email=email,
                        role=role,
                        firstName=firstName,
                        lastName=lastName,
                        password=generate_password_hash(password1, method="sha256"),
                        phoneNum=phoneNum,
                        gender=gender,
                        age=age,
                        SSN=SSN,
                        insurance=insurance,
                        houseNum=houseNum,
                        street=street,
                        city=city,
                        province=province,
                    )
                    db.session.add(new_user)
                    db.session.commit()
                    flash("Account Created Successfully")
                    return redirect(url_for("auth.login"))

    return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))


# @auth.route("/receptionistEditInfo/<String:username>", methods = ['GET','POST'])
# @login_required
# def receptionistEditInfo(username):

#   user_to_update= Patient.query.get_or_404(username)
#  if request.method == "POST":


@auth.route("/setPatientAppoi", methods=["GET", "POST"])
def setPatientAppoi():
    data = request.form
    print(data)

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        date = request.form.get("date")
        time = request.form.get("slot")
        room = request.form.get("room")
        appointmentType = request.form.get("appointmentType")
        branch = request.form.get("branch")
        status = request.form.get("status")

        new_appointment = Appointment(
            PatientUsername=username,
            date=date,
            time=time,
            roomAssigned=room,
            appointmentType=appointmentType,
            branch=branch,
            status=status,
        )
        db.session.add(new_appointment)
        db.session.commit()
        flash("Appointment Booked Successfully!")
        return redirect(url_for("views.receptionist"))

    return render_template("setPatientAppoi.html")
