from email.policy import default
from . import db

# from flask import UserMixin
from flask_login import UserMixin, current_user, login_required, login_user, logout_user
from sqlalchemy import func

## TO DO
# - add not null attributes, but this is probabaly already handled in sign up process.
# - Have a table for address as suggested by shannon, then refernce using foreign keys.
#   FOREIGN KEY(Street_num, Street_name, Postal_code) REFERENCES addresses(Street_num, Street_name, Postal_code));
#   But then how we deifferentiate between forewign keys of patients and employees
# - Have eseperate table for totCharge
# - Derive age from dob for Patient and employee.


class Patient(db.Model, UserMixin):
    tablename = "Patient"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    firstName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    phoneNum = db.Column(db.Integer, nullable=False)
    SSN = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(30), nullable=False)
    insurance = db.Column(db.String(50))
    # dob = db.Column(db.Date, nullable=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10), nullable=False)
    houseNum = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    province = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    appointments = db.relationship(
        "Appointment", backref="patient"
    )  # Makes accessing all patients appointments easier. Referncing class in relationship, we use uppper case names of classes
    payments = db.relationship("Payment", backref="patient")
    review = db.relationship(
        "Review", backref="patient", uselist=False
    )  # uselist=False declares one to one relationship
    record = db.relationship(
        "Record", backref="patient"
    )  # uselist=False declares one to one relationship


class Employee(db.Model, UserMixin):
    tablename = "Employee"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    firstName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    phoneNum = db.Column(db.Integer, nullable=False)
    SSN = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(30), nullable=False)
    insurance = db.Column(db.String(50))
    salary = db.Column(db.Numeric(2), default=0.00)
    age = db.Column(db.Integer)
    # dob = db.Column(db.Date, nullable=True)
    # signUpDate = db.Column(db.Date, default=func.now())   Automaticall creates dates of for us
    gender = db.Column(db.String(10), nullable=False)
    houseNum = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    province = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    # managesBranch = db.Column(db.Integer, db.ForeignKey('branch.branchId')) #$$$ one to one. Can be null, IDK CHECK IF CAUSES ERROR
    # managesBranch = db.relationship('Branch', backref='employee', uselist=False)
    worksInBranch = db.Column(
        db.Integer, db.ForeignKey("branch.branchId")
    )  # many to one
    appointments = db.relationship("Appointment", backref="employee")  # many to one


class Branch(db.Model):
    branchId = db.Column(db.Integer, primary_key=True)
    employeesNum = db.Column(db.Integer, nullable=False, default=0)
    branchName = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    province = db.Column(db.String(30), nullable=False)
    # branchManager = db.relationship('Employee', backref='branch') # one to one
    # branchManager = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    employees = db.relationship("Employee", backref="branch")  # one to many
    # employees = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False) # one to many


class Appointment(db.Model):
    appointmentId = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(30), nullable=False)
    dentistIdentifier = db.Column(
        db.String(30)
    )  # Maybe int? not sure if thats id or what
    appointmentType = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(20))
    roomAssigned = db.Column(db.String(20), nullable=False)
    date = db.Column(db.Date)
    startTime = db.Column(db.Time)
    endTime = db.Column(db.Time)
    treatment = db.relationship("Treatment", backref="appointment")
    feeCharge = db.relationship("FeeCharge", backref="appointment", uselist=False)
    patientUsername = db.Column(
        db.String(30), db.ForeignKey("patient.username"), nullable=False
    )  # one to many. Referncing to classes in foreignKey relationship, we use lower case name of class
    # Patient name can be accessed through FK referncing
    dentistIdneitifier = db.Column(
        db.Integer, db.ForeignKey("employee.id")
    )  # one to many


class Invoice(db.Model):
    invoiceId = db.Column(db.Integer, primary_key=True)
    dateOfIssue = db.Column(db.Date, default=func.now())
    discount = db.Column(db.Numeric(2), default=0.00)
    penalty = db.Column(db.Numeric(2), default=0.00)
    tax = db.Column(db.Numeric(2), default=0.00)
    payment = db.relationship("Payment", backref="invoice", uselist=False)
    feeCharge = db.relationship("FeeCharge", backref="invoice", uselist=False)


class FeeCharge(db.Model):
    feeId = db.Column(db.Integer, primary_key=True)
    patientCharge = db.Column(db.Numeric(2), default=0.00)
    insuranceCharge = db.Column(db.Numeric(2), default=0.00)
    totCharge = db.Column(db.Numeric(2), default=0.00)
    billId = db.Column(
        db.Integer, db.ForeignKey("payment.billId"), nullable=False
    )  # one to one
    invoiceId = db.Column(
        db.Integer, db.ForeignKey("invoice.invoiceId"), nullable=False
    )
    appointmentId = db.Column(
        db.Integer, db.ForeignKey("appointment.appointmentId"), nullable=False
    )  # one to one


class Payment(db.Model):
    billId = db.Column(db.Integer, primary_key=True)
    insuranceClaimId = db.Column(db.Integer)
    paymentType = db.Column(db.String(20), nullable=False)
    patientId = db.Column(db.Integer, db.ForeignKey("patient.id"))  # one to many
    invoiceId = db.Column(
        db.Integer, db.ForeignKey("invoice.invoiceId"), nullable=False
    )  # one to one


class Review(db.Model):
    reviewId = db.Column(db.Integer, primary_key=True)
    employeeProfessionalism = db.Column(db.String(100))
    value = db.Column(db.String(100))
    communication = db.Column(db.String(100))
    cleanliness = db.Column(db.String(100))
    patientId = db.Column(
        db.Integer, db.ForeignKey("patient.id"), nullable=False
    )  # one to many


class Procedure(db.Model):
    procedureID = db.Column(db.Integer, primary_key=True)
    procedureType = db.Column(db.String(50), nullable=False)
    procedureDescription = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date)
    treatmentId = db.Column(
        db.Integer, db.ForeignKey("treatment.treatmentId"), nullable=False
    )  # one to one
    appointmentId = db.Column(
        db.Integer, db.ForeignKey("appointment.appointmentId"), nullable=False
    )  # one to many


class Treatment(db.Model):
    treatmentId = db.Column(db.Integer, primary_key=True)
    treatmentType = db.Column(db.String(30), nullable=False)
    medication = db.Column(db.String(100))
    symptoms = db.Column(db.String(200), nullable=False)
    Teeth = db.Column(db.String(200), nullable=False)
    appointmentId = db.Column(
        db.Integer, db.ForeignKey("appointment.appointmentId"), nullable=False
    )  # one to many
    comments = db.relationship("Comment", backref="treatment")
    payments = db.relationship("Tooth", backref="treatment")
    procedure = db.relationship("Procedure", backref="treatment", uselist=False)


class Tooth(db.Model):
    toothName = db.Column(db.String(20), primary_key=True)
    treatmentId = db.Column(
        db.Integer, db.ForeignKey("treatment.treatmentId")
    )  # one ot many


class Comment(db.Model):
    commentId = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    treatmentId = db.Column(
        db.Integer, db.ForeignKey("treatment.treatmentId")
    )  # one ot many


class Record(db.Model):
    recordId = db.Column(db.Integer, primary_key=True)
    dateEdited = db.Column(
        db.Date, default=func.now()
    )  # Automaticall creates dates of for us
    patientId = db.Column(
        db.Integer, db.ForeignKey("patient.id"), nullable=False
    )  # one to one.
    progressNotes = db.relationship("ProgressNote", backref="Record", uselist=False)


class ProgressNote(db.Model):
    noteId = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(150), nullable=False)
    recordId = db.Column(db.Integer, db.ForeignKey("record.recordId"))  # many to one

