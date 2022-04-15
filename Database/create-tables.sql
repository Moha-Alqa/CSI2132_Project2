-- create a tables
CREATE TABLE Patient(
    Patient_ID int(9) PRIMARY KEY,
    Email VARCHAR(30) NOT NULL,
    Password VARCHAR(30) NOT NULL,
    First_name VARCHAR(30) NOT NULL,
    Last_name VARCHAR(30) NOT NULL,
  	Phone_num int(10) NOT NULL,
  	SSN int(9) NOT NULL,
  	Insurance VARCHAR(30) NOT NULL,
    Age VARCHAR(2) NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    Street_num int NOT NULL,
    Street_name VARCHAR(100) NOT NULL,
    Postal_code VARCHAR(30) NOT NULL,
    City VARCHAR(30) NOT NULL,
    Province VARCHAR(30) NOT NULL
    );
    
CREATE TABLE Appointment(
    Appointment_ID int(9) PRIMARY KEY,
  	Branch_ID int(9) NOT NULL,
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
	Comment_ID int(9) PRIMARY KEY,
    `Text` varchar(100),
    Treatment_ID int(9) NOT NULL
);
    

CREATE TABLE Branch(
	Branch_ID int(9) PRIMARY KEY,
    Employees_num int NOT NULL,
    Street_num int NOT NULL,
    Street_name VARCHAR(50) NOT NULL,
    City VARCHAR(100) NOT NULL,
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
    Age VARCHAR(2) NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    Street_num int NOT NULL,
    Street_name VARCHAR(100) NOT NULL,
    Province VARCHAR(100) NOT NULL,
    City VARCHAR(100) NOT NULL,
    Postal_code VARCHAR(20) NOT NULL,
    Branch_ID int(9) NOT NULL,
    Branch_manager VARCHAR(30) NOT NULL,
  	FOREIGN KEY(Branch_ID, Branch_manager) REFERENCES Branch(Branch_ID, Branch_manager)
    
);

--- create queries
INSERT INTO 'Patient'('id', 'username', 'email', `password`, 'firstName', 'lastName',
  	'phoneNum', 'SSN', 'role', 'insurance', 'age', 'gender', 'houseNum', 'street', 'City', 'province',
    ) VALUES ('1', 'sam', 'samantha25@gmail.com', '123', 'Samantha', 'Green', '6135608989', '167283432', 
    'ABCInsurance1', '25', 'Female', '1019', 'Acorn Street', 'Ottawa', 'Ontario');
    
INSERT INTO 'Patient'('Patient_ID', 'Email', `Password`, 'First_name', 'Last_name',
  	'Phone_num', 'SSN', 'Insurance', 'Age', 'Gender', 'Street_num', 'Street_name',
    'Postal_code', 'City', 'Province') VALUES ('345678932', 'tim88@gmail.com', 'Password!36', 
    'Timothy', 'Smith', '6132896790', '797886422', 'NewInsurance45', '88', 'Male',
    '38', 'Apple Street', 'K47 32F', 'Ottawa', 'Ontario');
    
INSERT INTO 'Patient'('Patient_ID', 'Email', `Password`, 'First_name', 'Last_name',
  	'Phone_num', 'SSN', 'Insurance', 'Age', 'Gender', 'Street_num', 'Street_name',
    'Postal_code', 'City', 'Province') VALUES ('892463789', 'alex@gmail.com', '6734J?', 
    'Alexander', 'Hernandez', '6135608989', '167283432', 'ABCInsurance1', '31', 'Male',
    '999', 'Brownspring Drive', 'KH6 32D', 'Ottawa', 'Ontario');

INSERT INTO 'Patient'('Patient_ID', 'Email', `Password`, 'First_name', 'Last_name',
  	'Phone_num', 'SSN', 'Insurance', 'Age', 'Gender', 'Street_num', 'Street_name',
    'Postal_code', 'City', 'Province') VALUES ('784628391', 'lilliantay66@gmail.com', 'Password45', 
    'Lillian', 'Taylor', '6138990943', '676789876', 'NewInsurance45', '66', 'Female',
    '1019', 'Bell Street ', 'K45 32J', 'Toronto', 'Ontario');
    
INSERT INTO 'Patient'('Patient_ID', 'Email', `Password`, 'First_name', 'Last_name',
  	'Phone_num', 'SSN', 'Insurance', 'Age', 'Gender', 'Street_num', 'Street_name',
    'Postal_code', 'City', 'Province') VALUES ('763290987', 'sarah00@gmail.com', 'Password!!23', 
    'Sarah', 'Mitchell', '6131523787', '898989095', 'OttawaInsurance8', '18', 'Female',
    '76', 'Tamerton Street', 'K54 FE3', 'London', 'Ontario');

INSERT INTO 'Patient'('Patient_ID', 'Email', `Password`, 'First_name', 'Last_name',
  	'Phone_num', 'SSN', 'Insurance', 'Age', 'Gender', 'Street_num', 'Street_name',
    'Postal_code', 'City', 'Province') VALUES ('383863625', 'ben10@gmail.com', 'ben8989!!23', 
    'Ben', 'Collins', '6135678781', '672451989', 'ABCInsurance1', '20', 'Male',
    '4501', 'Charlotte Street', 'K78 23H', 'Brampton', 'Ontario');
    
    
INSERT INTO 'Employee'('Employee_ID', 'Email', `Password`, 'First_name', 'Last_name',
      'Phone_num', 'SSN', 'Employee_role', 'Insurance', 'Salary', 'Age', 'Gender', 'Street_num', 'Street_name', 
      'Province', 'City', 'Postal_code', 'Branch_ID', 'Branch_manager') VALUES ('167823567', 'gail123@gmail.com', 'Password123', 'Gail',
      'Price', '4034598597', '659153957', 'Receptionist', 'Canada Life', '50000', '70', 'Female', '1741', 'Church Hill', 'ON', 'Ottawa', 
      'K1J 8N3', '214635515', 'Ashley Beaudry');
      
INSERT INTO 'Employee'('Employee_ID', 'Email', `Password`, 'First_name', 'Last_name',
      'Phone_num', 'SSN', 'Employee_role', 'Insurance', 'Salary', 'Age', 'Gender', 'Street_num', 'Street_name', 
      'Province', 'City', 'Postal_code', 'Branch_ID', 'Branch_manager') VALUES ('787898765', 'harry67@gmail.com', 'Password787!', 'Harry',
      'Williams', '5609898765', '674321689', 'Receptionist', 'Canada Life', '20000', '23', 'Male', '1027', 'Cheney Road', 'ON', 'Toronto', 
      'K4J 7N3', '214635515', 'Ashley Beaudry');

INSERT INTO 'Employee'('Employee_ID', 'Email', `Password`, 'First_name', 'Last_name',
      'Phone_num', 'SSN', 'Employee_role', 'Insurance', 'Salary', 'Age', 'Gender', 'Street_num', 'Street_name', 
      'Province', 'City', 'Postal_code', 'Branch_ID', 'Branch_manager') VALUES ('676764543', 'harriett@gmail.com', 'Password?!', 'Harriett',
      'Parker', '6136768909', '123456888', 'Receptionist', 'Canada Life', '45000', '41', 'Female', '999', '	Kendal Street', 'ON', 'Hamilton', 
      'K2F 8N6', '062076056', 'Andy Wong');
     
INSERT INTO 'Employee'('Employee_ID', 'Email', `Password`, 'First_name', 'Last_name',
      'Phone_num', 'SSN', 'Employee_role', 'Insurance', 'Salary', 'Age', 'Gender', 'Street_num', 'Street_name', 
      'Province', 'City', 'Postal_code', 'Branch_ID', 'Branch_manager') VALUES ('088059439', 'MelissaRose@gmail.com', 'Password845', 'Melissa',
      'Rose', '071410562', '844632496', 'Receptionist', 'Canada Life', '60000', '40', 'Female', '1741', 'Longfields Road', 'ON', 'Toronto', 
      'K1J 8N1', '018978171', 'Ashley Beaudry');
      
      
INSERT INTO 'Record'('Record_ID', 'Date_edited', 'Patient_ID', 
'Progress_note') VALUES ('123456657', '2022-04-10', '763290987', 'Teeth look ok');

INSERT INTO 'Record'('Record_ID', 'Date_edited', 'Patient_ID', 
'Progress_note') VALUES ('145467898', '2022-03-11', '12345678', 'Cavity in top row');

INSERT INTO 'Record'('Record_ID', 'Date_edited', 'Patient_ID', 
'Progress_note') VALUES ('676890987', '2022-04-03', '892463789', 'Need root canal');


INSERT INTO 'Branch'('Branch_ID', 'Employees_num', 'Street_num', 'Street_name', 'City', 'Province', 'Postal_code', 'Branch_manager')
            VALUES ('062076056', '3', '1428', 'Gladstone Avenue', 'Toronto', 'ON', 'K3J 9N2', 'Andy Wong');

INSERT INTO 'Branch'('Branch_ID', 'Employees_num', 'Street_num', 'Street_name', 'City', 'Province', 'Postal_code', 'Branch_manager')
            VALUES ('214635515', '3', '1428', 'Carlingwood Avenue', 'Toronto', 'ON', 'K3Y 9N2', 'Ashley Beaudry');
            
INSERT INTO 'Appointment'('Appointment_ID', 'Branch_ID', 'Dentist_identifier',
 'Appointment_type', `Status`, 'Room_assigned', 'Appointment_date',
  	'Start_time', 'End_time', 'Patient_ID') VALUES ('987654567', '214635515', 'Dentist',
  	'Teeth cleaning', 'Confirmed', 'Room 101', '2022-04-20', '14:00', '14:30', '383863625');
  	
INSERT INTO 'Appointment'('Appointment_ID', 'Branch_ID', 'Dentist_identifier',
 'Appointment_type', `Status`, 'Room_assigned', 'Appointment_date',
  	'Start_time', 'End_time', 'Patient_ID') VALUES ('44789199', '062076056', 'Dentist',
  	'Cavity Removal;', 'Confirmed', 'Room 113', '2022-05-01', '11:00', '11:30', '784628391');
  	
INSERT INTO 'Appointment_Procedure'('Appointment_ID', 'Patient_ID', 'Invoice_ID', 'Procedure_code', 'Procedure_type', 'Procedure_description',
    'Amount_of_procedures', 'Total_charge', 'Appointment_date', 'Insurance_claim_ID')
            VALUES ('987654567', '892463789', '345984356', '987634021', 'Veneers', 'custom-made shells of tooth-colored materials that covers surface of teeth to improve appearance',
                    '2', '10000', '2022-01-19', '183760987')
                    
INSERT INTO 'Appointment_Procedure'('Appointment_ID', 'Patient_ID', 'Invoice_ID', 'Procedure_code', 'Procedure_type', 'Procedure_description',
    'Amount_of_procedures', 'Total_charge', 'Appointment_date', 'Insurance_claim_ID')
            VALUES ('44789199', '763290987', '4829130876', '987634021', 'Teeth Cleaning', 'the removal of dental plaque from teeth with the intention of preventing tooth damage.',
                    '2', '10000', '2022-01-19', '183760987')
                                    
  	
SELECT * FROM Patient;
SELECT * FROM Employee;
SELECT * FROM Record;
SELECT * FROM Appointment;
SELECT * FROM Appointment_Procedure;

--- triggers, assertions and checks
