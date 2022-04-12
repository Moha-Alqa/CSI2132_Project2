#DROP DATABASE IF EXISTS CSI2132project;
CREATE DATABASE CSI2132project;

drop table if exists Patient cascade;
drop table if exists Appointment cascade;
drop table if exists Payment cascade;
drop table if exists Review cascade;
drop table if exists `User` cascade;
drop table if exists `Comment` cascade;
drop table if exists Employee cascade;
drop table if exists Tooth cascade;
drop table if exists ProgressNote cascade;
drop table if exists Treatment cascade;
drop table if exists Fee_Charge cascade;
drop table if exists Branch cascade;
drop table if exists Records cascade;
drop table if exists Appointment_Procedure cascade;
drop table if exists Invoice cascade;


CREATE TABLE Patient(
    Patient_ID int(9) PRIMARY KEY,
    Email VARCHAR(30) NOT NULL,
    `Password` VARCHAR(30) NOT NULL,
    First_name VARCHAR(30) NOT NULL,
    Last_name VARCHAR(30) NOT NULL,
  	Phone_num int(10) NOT NULL,
  	SSN int(9) NOT NULL,
  	Insurance VARCHAR(30) NOT NULL,
    /*Date_of_birth TIMESTAMP NOT NULL,*/
    Age varchar(2) NOT Null,
    Gender VARCHAR(20) NOT NULL,
    Street_num int NOT NULL,
    Street_name VARCHAR(100) NOT NULL,
    Postal_code VARCHAR(30) NOT NULL,
    City VARCHAR(30) NOT NULL,
    Province VARCHAR(30) NOT NULL
    );

CREATE TABLE Appointment(
    Appointment_ID int(9) PRIMARY KEY,
  	Branch VARCHAR(30) NOT NULL,
  	Dentist_identifier VARCHAR(30) NOT NULL,
  	Appointment_type VARCHAR(30) NOT NULL,
  	`Status` VARCHAR(30) NOT NULL,
  	Room_assigned VARCHAR(30) NOT NULL,
  	Appointment_date DATE NOT NULL,
  	Start_time TIMESTAMP NOT NULL,
    End_time TIMESTAMP NOT NULL,
  	Patient_ID int(9) NOT NULL,
    FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID)
    );


CREATE TABLE Payment(
    Bill_ID int(9) PRIMARY KEY,
    Patient_ID int(9) NOT NULL,
    Appointment_ID int(9) NOT NULL,
    Procedure_ID int(9) NOT NULL,
	Patient_charge  decimal(9,2) NOT NULL DEFAULT '0.00',
    Insurance_charge  decimal(9,2) NOT NULL DEFAULT '0.00',
    Insurance_claim_ID int(9) NOT NULL,
    Payment_type VARCHAR(20) NOT NULL,
    FOREIGN KEY(Appointment_ID) REFERENCES Appointment(Appointment_ID),
    FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Review(
	Review_ID int(9) PRIMARY KEY,
    Employee_professionalism VARCHAR(100) NOT NULL,
  	Value VARCHAR(100) NOT NULL,
  	Communication VARCHAR(100) NOT NULL,
  	Cleanliness VARCHAR(20) NOT NULL,
    Patient_ID int(9) NOT NULL,
  	FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE `User`(
    Username VARCHAR(50) PRIMARY KEY,
    `Password` VARCHAR(50) NOT NULL,
    `Role` VARCHAR(20) NOT NULL,
    Email VARCHAR(30) NOT NULL

);

CREATE TABLE Employee(
    Employee_ID int(9) PRIMARY KEY,
    Email VARCHAR(30) NOT NULL,
    `Password` VARCHAR(30) NOT NULL,
    First_name VARCHAR(30) NOT NULL,
    Last_name VARCHAR(30) NOT NULL,
    Phone_num int(10) NOT NULL,
    SSN int(9) NOT NULL,
    Employee_role VARCHAR(50) NOT NULL,
    Insurance VARCHAR(50) NOT NULL,
    Salary decimal(10,2) NOT NULL DEFAULT '0.00',
    Age varchar(2) NOT Null,
    /*Date_of_birth TIMESTAMP NOT NULL,*/
    Gender VARCHAR(20) NOT NULL,
    Street_num int NOT NULL,
    Street_name VARCHAR(100) NOT NULL,
    Province VARCHAR(100) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Postal_code VARCHAR(20) NOT NULL,
    Branch_manager VARCHAR(20) NOT NULL,
  	FOREIGN KEY(Branch_manager) REFERENCES Branch(Branch_manager)
    
);

CREATE TABLE Treatment(
	Treatment_ID int PRIMARY KEY,
    Treatment_type VARCHAR(30) NOT NULL,
    Appointment_ID int(9) NOT NULL,
    Medication VARCHAR(100) NOT NULL,
    Symptoms VARCHAR(200) NOT NULL,
    Tooth VARCHAR(200) NOT NULL,
    Patient_condition VARCHAR(50) NOT NULL,
    FOREIGN KEY(Appointment_ID) REFERENCES Appointment(Patient_ID)
);

CREATE TABLE Fee_Charge(
	Fee_charge_ID int(9) PRIMARY KEY,
    Patient_charge decimal(9,2) NOT NULL,
    Insurance decimal(9,2) NOT NULL,
    Total_charge decimal(9,2) NOT NULL,
    Bill_ID int(9) NOT NULL,
	Appointment_ID int(9) NOT NULL,
    FOREIGN KEY(Appointment_ID) REFERENCES Appointment(Patient_ID)
);

CREATE TABLE Tooth(
	Tooth_name VARCHAR(100) NOT NULL,
    Treatment_ID int(9) NOT NULL
    );

CREATE TABLE `Comment`(
	Comment_ID int PRIMARY KEY,
    `Text` varchar(100),
    Treatment_ID int(9) NOT NULL
);
    

CREATE TABLE Branch(
	Branch_ID int(9) PRIMARY KEY,
    Employees_num int NOT NULL,
    Street_num int NOT NULL,
    Street_name VARCHAR(50) NOT NULL,
    City VARCHAR(100) PRIMARY KEY,
    Province VARCHAR(100) NOT NULL,
    Postal_code VARCHAR(30) NOT NULL,
    Branch_manager VARCHAR(30) NOT NULL
);

CREATE TABLE Record(
    Record_ID int(9) PRIMARY KEY,
    Date_edited DATE NOT NULL,
    Patient_ID int(9) NOT NULL,
    Progress_note VARCHAR(100) NOT NULL,
    FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID)
);

CREATE TABLE Appointment_Procedure(
    Appointment_ID int(9) NOT NULL,
    Patient_ID int(9) NOT NULL,
    Invoice_ID int NOT NULL,
    Procedure_code int NOT NULL,
    Procedure_type VARCHAR(50) NOT NULL,
    Procedure_description VARCHAR(50) NOT NULL,
    Amount_of_procedures INT NOT NULL,
    Total_charge decimal(9,2) NOT NULL DEFAULT '0.00',
    Appointment_date TIMESTAMP NOT NULL,
    Insurance_claim_ID int(9) NOT NULL,
    FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID),
    FOREIGN KEY(Appointment_ID) REFERENCES Appointment(Patient_ID),
    FOREIGN KEY(Invoice_ID) REFERENCES Invoice(Invoice_ID)
);
    

CREATE TABLE Invoice(
    Invoice_ID int PRIMARY KEY,
    Date_of_issue TIMESTAMP NOT NULL,
  	Discount decimal(9,2) NOT NULL DEFAULT '0.00',
  	Penalty decimal(9,2) NOT NULL DEFAULT '0.00',
  	Tax decimal(9,2) NOT NULL DEFAULT '0.00',
  	Fee_charge_ID int(9) NOT NULL,
  	FOREIGN KEY(Fee_charge_ID) REFERENCES Fee_Charge(Fee_charge_ID)
);

CREATE TABLE ProgressNote(
    Note_ID int PRIMARY KEY,
    Note VARCHAR(100) NOT NULL,
    Record_ID int(9) NOT NULL
);