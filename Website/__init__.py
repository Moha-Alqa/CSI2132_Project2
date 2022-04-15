import datetime
from flask import Flask
from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager
from requests import session
from werkzeug.security import generate_password_hash
from sqlalchemy import func

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

    login_manager = LoginManager()
    login_manager.login_view = 'view.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_patient(id):
        return Patient.query.get(int(id))

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_preffix="/")

    return app


def create_database(app):
    if not path.exists("Website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")

        from .models import Patient, Employee, Branch, Appointment, Procedure, Tooth, Comment, Treatment, Record, ProgressNote, Invoice, FeeCharge, Payment


        ###### --------------------------------------- POPULATING RELATIONS --------------------------------------- ######    
        
           
        with app.app_context():
            p1 = Patient(id='748374639', username='james3', email="james3@gmail.com", password=generate_password_hash("iwhge94", method="sha256"), firstName="James", lastName="Garcia", phoneNum='6472480571', SSN='789176415', role="Patient", insurance="CanadaLife", age=21, gender="Male", houseNum="1127", street="Trinity Street", province="Ontario", city="Ottawa")
            p2 = Patient(id='949374839', username='rob2', email="rob2@gmail.com", password=generate_password_hash("4iuwgrnvw", method="sha256"), firstName="Robert", lastName="Miller", phoneNum='6483516970', SSN=198965138, role="Patient", insurance="abcInsurance", age=83, gender="Male", houseNum="12", street="Twining Street", province="Ontario", city="Toronto")
            p3 = Patient(id='759394732', username='charl3', email="charl3@gmail.com", password=generate_password_hash("784iwug", method="sha256"), firstName="Charlotte", lastName="Davis", phoneNum='6108987043', SSN=187091016, role="Patient", insurance="lightInsurance", age=30, gender="Female", houseNum="65", street="Underwood Street", province="Ontario", city="Mississauga")
            p4 = Patient(id='643973947', username='soph2', email="msoph2@gmail.com", password=generate_password_hash("29384iurjk", method="sha256"), firstName="Sophia", lastName="Rodriguez", phoneNum='6703780878', SSN=222345328, role="Patient", insurance="newInsurance", age=45, gender="Female", houseNum="662", street="Bryan Road", province="Ontario", city="Ottawa")
            p5 = Patient(id='734659454', username='mike66', email="mike66@gmail.com", password=generate_password_hash("9gine", method="sha256"), firstName="Michael", lastName="Brown", phoneNum='6123458869', SSN=123226453, role="Patient", insurance="CanadaLife", age=46, gender="Male", houseNum="891", street="Apothecary Street", province="Ontario", city="Mississauga")
            p6 = Patient(id='574838548', username='joe55', email="joe55@gmail.com", password=generate_password_hash("47ituwgh", method="sha256"), firstName="Joseph", lastName="Johnson", phoneNum='9473280059', SSN=829822909, role="Patient", insurance="abcInsurance", age=21, gender="Male", houseNum="1156", street="Dickens Square", province="Ontario", city="Ottawa")
            p7 = Patient(id='753874578', username='eliz2', email="eliz2@gmail.com", password=generate_password_hash("9irneg", method="sha256"), firstName="Elizabeth", lastName="MacDonald", phoneNum='9473420887', SSN=889876162, role="Patient", insurance="abcInsurance", age=24, gender="Female", houseNum="111", street="Farren Road", province="Ontario", city="Ottawa")
            p8 = Patient(id='754985345', username='elen7', email="elen7@gmail.com", password=generate_password_hash("g984eu", method="sha256"), firstName="Eleanor", lastName="Martin", phoneNum='3433400079', SSN=113992276, role="Patient", insurance="lightInsurance", age=26, gender="Female", houseNum="123", street="Coalecroft Road", province="Ontario", city="Kingston")
            p9 = Patient(id='576454999', username='an4', email="an4@gmail.com", password=generate_password_hash("09ijig", method="sha256"), firstName="Anthony", lastName="Tremblay", phoneNum='3880987053', SSN=338800554, role="Patient", insurance="abcInsurance", age=36, gender="Male", houseNum="567", street="Vernon Rise", province="Ontario", city="Kingston")
            p10 = Patient(id='877594839', username='s02', email="s02@gmail.com", password=generate_password_hash("i3ueng", method="sha256"), firstName="Steven", lastName="Smith", phoneNum='5485598799', SSN=100443009, role="Patient", insurance="CanadaLife", age=19, gender="Male", houseNum="435", street="Scholey Cottages", province="Ontario", city="London")
            p11 = Patient(id='787890904', username='lea2', email="lea2@gmail.com", password=generate_password_hash("kwejfn3", method="sha256"), firstName="Leah", lastName="Roy", phoneNum='6130051905', SSN=800767666, role="Patient", insurance="abcInsurance", age=21, gender="Female", houseNum="982", street="Chillingworth Road", province="Ontario", city="Ottawa")
            p12 = Patient(id='909874635', username='no3', email="no3@gmail.com", password=generate_password_hash("84uh", method="sha256"), firstName="Naomi", lastName="Fortin", phoneNum='1345782020', SSN=198141321, role="Patient", insurance="lightInsurance", age=28, gender="Female", houseNum="1233", street="Hoxton Street", province="Ontario", city="Kingston")
            p13 = Patient(id='784390947', username='jacob7', email="jacob7@gmail.com", password=generate_password_hash("oheinrj4", method="sha256"), firstName="Jacob", lastName="Ramírez", phoneNum='6879092246', SSN=113345556, role="Patient", insurance="lightInsurance", age=55, gender="Male", houseNum="2052", street="Vivian Grove", province="Ontario", city="Ottawa")
            p14 = Patient(id='777443289', username='eric2', email="eric2@gmail.com", password=generate_password_hash("3i4uhkjg", method="sha256"), firstName="Eric", lastName="Gagné", phoneNum='8835558607', SSN=555166778, role="Patient", insurance="newInsurance", age=62, gender="Male", houseNum="1073", street="Grant Street", province="Ontario", city="Toronto")
            p15 = Patient(id='123875490', username='alex23', email="alex23@gmail.com", password=generate_password_hash("sljdg", method="sha256"), firstName="Alexis", lastName="White", phoneNum='6473480879', SSN=789876435, role="Patient", insurance="CanadaLife", age=21, gender="Female", houseNum="1027", street="Abbey Road", province="Ontario", city="Ottawa")
            p16 = Patient(id='456783942', username='henry45', email="henry45@gmail.com", password=generate_password_hash("skgb78", method="sha256"), firstName="Henry", lastName="Thompson", phoneNum='6473586979', SSN=898765438, role="Patient", insurance="abcInsurance", age=88, gender="Male", houseNum="32", street="Alexander Street", province="Ontario", city="Toronto")
            p17 = Patient(id='134589876', username='kay1', email="kaylallen23@gmail.com", password=generate_password_hash("ghsbdfe67", method="sha256"), firstName="Kayla", lastName="Allen", phoneNum='6138987643', SSN=987098096, role="Patient", insurance="lightInsurance", age=30, gender="Female", houseNum="65", street="Bond Street", province="Ontario", city="Mississauga")
            p18 = Patient(id='122343456', username='m456', email="meg23@gmail.com", password=generate_password_hash("hsgeiuh78", method="sha256"), firstName="Megan", lastName="King", phoneNum='6373480878', SSN=112345328, role="Patient", insurance="newInsurance", age=45, gender="Female", houseNum="662", street="Malvern Terrace", province="Ontario", city="Ottawa")
            p19 = Patient(id='423444993', username='w234', email="will56@gmail.com", password=generate_password_hash("jvdbhse2", method="sha256"), firstName="William", lastName="Scott", phoneNum='6133450869', SSN=123456453, role="Patient", insurance="CanadaLife", age=44, gender="Male", houseNum="892", street="Martin Street", province="Ontario", city="Mississauga")
            p20 = Patient(id='423444190', username='tom66', email="tom67@gmail.com", password=generate_password_hash("osebge3", method="sha256"), firstName="Thomas", lastName="Torres", phoneNum='4732805590', SSN=129899909, role="Patient", insurance="abcInsurance", age=22, gender="Male", houseNum="1056", street="Hope Street", province="Ontario", city="Ottawa")
            p21 = Patient(id='623454322', username='abby77', email="abby32@gmail.com", password=generate_password_hash("ryiwgbfe67", method="sha256"), firstName="Abigail", lastName="Wright", phoneNum='6473484889', SSN=999876665, role="Patient", insurance="abcInsurance", age=24, gender="Female", houseNum="111", street="Grove Road", province="Ontario", city="Ottawa")
            p22 = Patient(id='923444189', username='tammy54', email="tammy65@gmail.com", password=generate_password_hash("juehfw3", method="sha256"), firstName="Tamara", lastName="Flores", phoneNum='6433420179', SSN=112998876, role="Patient", insurance="lightInsurance", age=26, gender="Female", houseNum="123", street="Glebe Road", province="Ontario", city="Kingston")
            p23 = Patient(id='525464100', username='a23', email="andy3@gmail.com", password=generate_password_hash("jhvbre32", method="sha256"), firstName="Andrew", lastName="Green", phoneNum='9888987653', SSN=998866554, role="Patient", insurance="abcInsurance", age=36, gender="Male", houseNum="567", street="Frederick Street", province="Ontario", city="Kingston")
            p24 = Patient(id='623324166', username='alex45', email="alex32@gmail.com", password=generate_password_hash("hjsge2", method="sha256"), firstName="Alexander", lastName="Nelson", phoneNum='9488898799', SSN=124443989, role="Patient", insurance="CanadaLife", age=19, gender="Male", houseNum="435/22", street="Cambridge Street", province="Ontario", city="London")
            p25 = Patient(id='522444144', username='l99o', email="lous32@gmail.com", password=generate_password_hash("894643", method="sha256"), firstName="Lousie", lastName="Nguyen", phoneNum='6134458906', SSN=888777666, role="Patient", insurance="abcInsurance", age=25, gender="Female", houseNum="989", street="Newcastle Street", province="Ontario", city="Ottawa")
            p26 = Patient(id='633454199', username='tyler45', email="ty90@gmail.com", password=generate_password_hash("87t4whge", method="sha256"), firstName="Tyler", lastName="Hall", phoneNum='6134578904', SSN=898743321, role="Patient", insurance="lightInsurance", age=22, gender="Male", houseNum="1333", street="Cobden Street", province="Ontario", city="Kingston")
            p27 = Patient(id='623444166', username='zane33', email="zane23@gmail.com", password=generate_password_hash("giu3wnes", method="sha256"), firstName="Zane", lastName="Rivera", phoneNum='7879093242', SSN=113344556, role="Patient", insurance="lightInsurance", age=55, gender="Male", houseNum="1052", street="Emily Place", province="Ontario", city="Ottawa")
            p28 = Patient(id='145994198', username='harry66', email="harry66@gmail.com", password=generate_password_hash("8473it", method="sha256"), firstName="Harry", lastName="Carter", phoneNum='6135558999', SSN=555666778, role="Patient", insurance="newInsurance", age=62, gender="Male", houseNum="1013", street="Bromley Street", province="Ontario", city="Toronto")
            p29 = Patient(id='991234441', username='sarah23', email="sarahrob65@gmail.com", password=generate_password_hash("948grseg", method="sha256"), firstName="Sarah", lastName="Roberts", phoneNum='9002378771', SSN=999333666, role="Patient", insurance="newInsurance", age=78, gender="Female", houseNum="22", street="Chapel Street", province="Ontario", city="Mississauga")
            p30 = Patient(id='871235441', username='nat11', email="natalie111@gmail.com", password=generate_password_hash("sknbee", method="sha256"), firstName="Natalie", lastName="Adams", phoneNum='9887655355', SSN=888777091, role="Patient", insurance="lightInsurance", age=90, gender="Female", houseNum="452", street="Buckingham Terrace", province="Ontario", city="London")
            

            d1 = Employee(id='567898763', username='dan34', firstName='Daniel', lastName='Elliot', email="dan77@gmail.com", password=generate_password_hash("hgdyeuw78", method="sha256"), phoneNum=6134567834, SSN=233445423, role="Dentist", insurance="lightInsurance", age=40, gender="Male", houseNum="1111", street="New Street", province="Ontario", city="Ottawa",worksInBranch='7878984327')
            d2 = Employee(id='676789832', username='ash88', firstName='Ashley', lastName='Lopez', email="lopez67@gmail.com", password=generate_password_hash("wkughy7", method="sha256"), phoneNum=7645332987, SSN=567439087, role="Dentist", insurance="abcInsurance", age=30, gender="Female", houseNum="1099", street="Parliament Street", province="Ontario", city="Ottawa",worksInBranch='7878984327')
            d3 = Employee(id='123219008', username='sam22', firstName='Samantha', lastName='Wilson', email="sam23@gmail.com", password=generate_password_hash("sjegyh67", method="sha256"), phoneNum=5487659489, SSN=764398754, role="Dentist", insurance="CanadaLife", age=33, gender="Female", houseNum="2054", street="Red Lion Street", province="Ontario", city="Kingston",worksInBranch='5443337786')
            d4 = Employee(id='223348987', username='tom87', firstName='Thomas', lastName='Taylor', email="t55@gmail.com", password=generate_password_hash("kwue22", method="sha256"), phoneNum=3214576859, SSN=754398654, role="Dentist", insurance="abcInsurance", age=39, gender="Male", houseNum="779", street="St. John's Road", province="Ontario", city="Kingston",worksInBranch='5443337786')
            d5 = Employee(id='454234900', username='kim999', firstName='Kim', lastName='Lee', email="kim88@gmail.com", password=generate_password_hash("nbduir7", method="sha256"), phoneNum=3214577788, SSN=564739823, role="Dentist", insurance="CanadaLife", age=60, gender="Female", houseNum="890", street="Dominion Street", province="Ontario", city="Toronto",worksInBranch='7878984327')
            d6 = Employee(id='343487643', username='ezra33', firstName='Ezra', lastName='Gomez', email="ezra44@gmail.com", password=generate_password_hash("444tiwuhg", method="sha256"), phoneNum=8980009943, SSN=934568764, role="Dentist", insurance="newInsurance", age=42, gender="Male", houseNum="32", street="Bishop's Terrace", province="Ontario", city="Toronto", worksInBranch= '4443329874')
            

            r1 = Employee(id='565678498', username='jane44', firstName='Jane', lastName='Doe', email="jane45@gmail.com", password=generate_password_hash("iervb54", method="sha256"), phoneNum=6124557835, SSN=777665498, role="Receptionist", insurance="CanadaLife", age=40, gender="Female", houseNum="1113", street="Southern Grove", province="Ontario", city="Mississauga")
            r2 = Employee(id='453289876', username='j65', firstName='John', lastName='Smith', email="john32@gmail.com", password=generate_password_hash("79545tgnr", method="sha256"), phoneNum=4548987650, SSN=432345786, role="Receptionist", insurance="CanadaLife", age=30, gender="Male", houseNum="7049", street="Handley Street", province="Ontario", city="London")

            b1 = Branch(branchId='7878984327', employeesNum=6, branchName='DentaiGo', street='Lucas Road', city='Ottawa', province='Ontario')
            b2 = Branch(branchId='5443337786', employeesNum=5, branchName='DentaiSit', street='Smith Street', city='Kingston', province='Ontario')
            b3 = Branch(branchId='4443329874', employeesNum=6, branchName='DentaiShine', street='Turner Road', city='Toronto', province='Ontario')

            pr1 = Procedure(procedureID='878787656', procedureType = 'Root Canal', procedureDescription = 'removal of bacteria from an infected root canal.', date=datetime.datetime(2022, 6, 10), treatmentId='989000008', appointmentId='000000001')
            pr2 =  Procedure(procedureID='787899000', procedureType = 'Crown Placement', procedureDescription = 'clear away any decal and shave down the tooth with cavity and place crown.', date=datetime.datetime(2022, 7, 11), treatmentId='111333287', appointmentId='000000002')

            t1 = Tooth(toothName='Mandibullar Left Third Molar', treatmentId = '989000008')
            t2 = Tooth(toothName='Maxillary Right Central Incisor', treatmentId = '111333287')

            c1 = Comment(commentId='555666777', text='Everything looks ok')
            c2 = Comment(commentId='332876897', text='There is a cavity')
            c3 = Comment(commentId='900000054', text='Braces reccommended')

            tr1 = Treatment(treatmentId='989000008',treatmentType='Root Canal Treatment', medication='(OTC) pain medication',symptoms='tooth discoloration', Teeth='Mandibullar Left Third Molar', appointmentId='000000001')
            tr2 = Treatment(treatmentId='111333287',treatmentType='Crown Treatment', medication='Acetaminophen', symptoms='mild pain', Teeth='All', appointmentId='000000002')

            re1 = Record(recordId='666543898', dateEdited=datetime.datetime(2022, 3, 10), patientId='871235441')
            re2 = Record(recordId='776644309', dateEdited=datetime.datetime(2022, 2, 20), patientId='991234441')
            re3 = Record(recordId='900008764', dateEdited=datetime.datetime(2022, 1, 4), patientId='145994198')

            pn1 = ProgressNote(noteId='777888430', note='Teeth look ok', recordId='666543898')
            pn2 = ProgressNote(noteId='800000439', note='There is a cavity', recordId='776644309')
            pn3 = ProgressNote(noteId='400000434', note='Braces reccomended', recordId='900008764')

            app1=Appointment(appointmentId='000000001', branch='7878984327', appointmentType='check-up', status='booked', roomAssigned='Room101', date=datetime.datetime(2022, 6, 10), startTime= datetime.time(11,0,0), endTime = datetime.time(11,30,0), patientUsername='james3', dentistIdneitifier='567898763')
            app2=Appointment(appointmentId='000000002', branch='7878984327', appointmentType='check-up', status='booked', roomAssigned='Room104', date=datetime.datetime(2022, 7, 11), startTime= datetime.time(2,0,0), endTime = datetime.time(2,30,0), patientUsername='james3', dentistIdneitifier='676789832')
            app3=Appointment(appointmentId='000000003', branch='5443337786', appointmentType='check-up', status='booked', roomAssigned='Room301', date=datetime.datetime(2022, 8, 25), startTime= datetime.time(11,0,0), endTime = datetime.time(11,30,0), patientUsername='james3', dentistIdneitifier='123219008')
            app4=Appointment(appointmentId='000000004', branch='5443337786', appointmentType='check-up', status='booked', roomAssigned='Room53', date=datetime.datetime(2022, 8, 5), startTime= datetime.time(2,0,0), endTime = datetime.time(2,30,0), patientUsername='rob2', dentistIdneitifier='567898763')
            app5=Appointment(appointmentId='000000005', branch='4443329874', appointmentType='check-up', status='booked', roomAssigned='Room106', date=datetime.datetime(2022, 7, 27), startTime= datetime.time(11,0,0), endTime = datetime.time(11,30,0), patientUsername='rob2', dentistIdneitifier='454234900')
            app6=Appointment(appointmentId='000000006', branch='4443329874', appointmentType='check-up', status='booked', roomAssigned='Room109', date=datetime.datetime(2022, 6, 9), startTime= datetime.time(1,0,0), endTime = datetime.time(1,30,0), patientUsername='rob2', dentistIdneitifier='343487643')

            i1 = Invoice(invoiceId='100000001', dateOfIssue=datetime.datetime(2022, 6, 10), discount='0.0', penalty='0.0', tax= '0.13')
            i2 = Invoice(invoiceId='100000002', dateOfIssue=datetime.datetime(2022, 7, 11), discount='0.0', penalty='0.0', tax= '0.13')
            i3 = Invoice(invoiceId='100000003', dateOfIssue=datetime.datetime(2022, 8, 25), discount='0.0', penalty='0.0', tax= '0.13')

            f1 = FeeCharge(feeId='200000001', patientCharge='9.99', insuranceCharge='209.65', totCharge='219.64', billId='', invoiceId='100000001', appointmentId='000000001')
            f2 = FeeCharge(feeId='200000002', patientCharge='39.99', insuranceCharge='500.27', totCharge='540.26', billId='', invoiceId='100000002', appointmentId='000000002')
            f3 = FeeCharge(feeId='200000003', patientCharge='50.99', insuranceCharge='305.66', totCharge='356.65', billId='', invoiceId='100000003', appointmentId='000000003')

            pay1= Payment(billId='777777777', insuranceClaimId='777777771', paymentType='Mastercard', patientId='923444189', invoiceId='100000001')
            pay2= Payment(billId='555555555', insuranceClaimId='555555551', paymentType='Debit', patientId='871235441', invoiceId='100000002')
            pay3= Payment(billId='888888888', insuranceClaimId='888888881', paymentType='Cash', patientId='123219008', invoiceId='100000003')

            # add patients
            db.session.add(p1)
            db.session.add(p2)
            db.session.add(p3)
            db.session.add(p4)
            db.session.add(p5)
            db.session.add(p6)
            db.session.add(p7)
            db.session.add(p8)
            db.session.add(p9)
            db.session.add(p10)
            db.session.add(p11)
            db.session.add(p12)
            db.session.add(p13)
            db.session.add(p14)
            db.session.add(p15)
            db.session.add(p16)
            db.session.add(p17)
            db.session.add(p18)
            db.session.add(p19)
            db.session.add(p20)
            db.session.add(p21)
            db.session.add(p22)
            db.session.add(p23)
            db.session.add(p24)
            db.session.add(p25)
            db.session.add(p26)
            db.session.add(p27)
            db.session.add(p28)
            db.session.add(p29)
            db.session.add(p30)

            #add dentists
            db.session.add(d1)
            db.session.add(d2)
            db.session.add(d3)
            db.session.add(d4)
            db.session.add(d5)
            db.session.add(d6)

            #add receptionists
            db.session.add(r1)
            db.session.add(r2)

            #add branches
            db.session.add(b1)
            db.session.add(b2)
            db.session.add(b3)

            #add procedures
            db.session.add(pr1)
            db.session.add(pr2)

            #add treatment
            db.session.add(tr1)
            db.session.add(tr2)          

            #add tooth
            db.session.add(t1)
            db.session.add(t2)    

            #add comment
            db.session.add(c1)
            db.session.add(c2)
            db.session.add(c3)

            #add records
            db.session.add(re1)
            db.session.add(re2)
            db.session.add(re3)

            #add progress notes
            db.session.add(pn1)
            db.session.add(pn2)
            db.session.add(pn3)

            #add appointments
            db.session.add(app1)
            db.session.add(app2)
            db.session.add(app3)      
            db.session.add(app4)
            db.session.add(app5)
            db.session.add(app6) 

            #add invoice
            db.session.add(i1)
            db.session.add(i2)
            db.session.add(i3)

            #add payment
            db.session.add(pay1)
            db.session.add(pay2)
            db.session.add(pay3)       

            #add fee charge
            db.session.add(f1)
            db.session.add(f2)
            db.session.add(f3)   
                    
            db.session.commit()


            ###### --------------------------------------- QUERIES --------------------------------------- ######

            ### 1 Show the list dentists in each branch.
            # Sort dentists by branch they work in
            bra1 = (db.session.query(Branch, Employee).filter(Employee.worksInBranch == Branch.branchId).order_by(Branch.branchId).all())
            # Show dentists working in branch with id '7878984327'
            bra2 = (db.session.query(Branch, Employee).filter(Employee.worksInBranch == Branch.branchId).filter(Branch.branchId == "7878984327").order_by(Branch.branchId).all())
            # Show dentists working in branch with id '5443337786'
            bra3 = (db.session.query(Branch, Employee).filter(Employee.worksInBranch == Branch.branchId).filter(Branch.branchId == "5443337786").order_by(Branch.branchId).all())

            ### 2 Add new patients
            pat1 = Patient(id='748374439', username='jmes3', email="jamees3@gmail.com", password=generate_password_hash("iwhge94", method="sha256"), firstName="James", lastName="Garcia", phoneNum='6472480571', SSN='789176415', role="Patient", insurance="CanadaLife", age=21, gender="Male", houseNum="1127", street="Trinity Street", province="Ontario", city="Ottawa")
            pat2 = Patient(id='949374239', username='rb2', email="rob22@gmail.com", password=generate_password_hash("4iuwgrnvw", method="sha256"), firstName="Robert", lastName="Miller", phoneNum='6483516970', SSN=198965138, role="Patient", insurance="abcInsurance", age=83, gender="Male", houseNum="12", street="Twining Street", province="Ontario", city="Toronto")
            pat3 = Patient(id='759394132', username='carl3', email="charl33@gmail.com", password=generate_password_hash("784iwug", method="sha256"), firstName="Charlotte", lastName="Davis", phoneNum='6108987043', SSN=187091016, role="Patient", insurance="lightInsurance", age=30, gender="Female", houseNum="65", street="Underwood Street", province="Ontario", city="Mississauga")

            ### 3 Check upcoming appointment with the dentist
            # check upcoming appointment with dentist with id 567898763 and 676789832 (2 seperate queris)
            appoint1 = (db.session.query(Appointment).filter(Appointment.dentistIdneitifier == 567898763).all())
            appoint2 = (db.session.query(Appointment).filter(Appointment.dentistIdneitifier == 676789832).all())

            ### 4. Set a new appointment 
            appp1=Appointment(appointmentId='000000010', branch='7878984327', appointmentType='check-up', status='booked', roomAssigned='Room101', date=datetime.datetime(2022, 6, 10), startTime= datetime.time(11,0,0), endTime = datetime.time(11,30,0), patientUsername='james3', dentistIdneitifier='567898763')
            appp2=Appointment(appointmentId='000000020', branch='7878984327', appointmentType='check-up', status='booked', roomAssigned='Room104', date=datetime.datetime(2022, 7, 11), startTime= datetime.time(2,0,0), endTime = datetime.time(2,30,0), patientUsername='rb2', dentistIdneitifier='676789832')

            ### 5.Add a new employee
            den1 = Employee(id='567898063', username='dann34', firstName='Daniel', lastName='Elliot', email="dan777@gmail.com", password=generate_password_hash("hgdyeuw78", method="sha256"), phoneNum=6134567834, SSN=233445423, role="Dentist", insurance="lightInsurance", age=40, gender="Male", houseNum="1111", street="New Street", province="Ontario", city="Ottawa",worksInBranch='7878984327')
            den2 = Employee(id='676781832', username='assh88', firstName='Ashley', lastName='Lopez', email="lopez677@gmail.com", password=generate_password_hash("wkughy7", method="sha256"), phoneNum=7645332987, SSN=567439087, role="Dentist", insurance="abcInsurance", age=30, gender="Female", houseNum="1099", street="Parliament Street", province="Ontario", city="Ottawa",worksInBranch='7878984327')

            ### 6. Check the types of procedures available
            # proc = (db.session.query(Procedure).filter(func.distinct(Procedure.procedureType)).all())

