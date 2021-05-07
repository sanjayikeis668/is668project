
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, UserMixin, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
#from flask_migrate import Migrate
from flask import flash
from sqlalchemy import func




app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="iyke7763",
    password="Ikechukwu5020!",
    hostname="iyke7763.mysql.pythonanywhere-services.com",
    databasename="iyke7763$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
#migrate = Migrate(app, db)

app.secret_key = "Ikechukwu"
login_manager = LoginManager()
login_manager.init_app(app)

param = ["SEX", "RACE"]

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))





    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def get_id(self):
        return self.username



@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    posted = db.Column(db.DateTime, default=datetime.now)
    commenter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    commenter = db.relationship('User', foreign_keys=commenter_id)

class Students(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(4096))
    lname = db.Column(db.String(4096))
    major = db.Column(db.String(4096))
    email = db.Column(db.String(4096))
    assignment = db.relationship('Assignments', backref='students')


class Assignments(db.Model):
    __tablename__ = "assignments"

    id = db.Column(db.Integer, primary_key=True)
    assignmentname = db.Column(db.String(4096))
    grade = db.Column(db.Integer)
    classname = db.Column(db.String(4096))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    scholar = db.relationship('Students', foreign_keys=student_id)




@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main.html", comments=Comment.query.all())

    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    comment = Comment(content=request.form["contents"], commenter=current_user)
    db.session.add(comment)
    db.session.commit()
    flash('Item added')
    return redirect(url_for('index'))

@app.route('/homework', methods=["GET", "POST"])
def homework():
    if request.method == "GET":
        return render_template('homework.html', params = param)

    getparam = request.form.get("parameters")
    getString = "get=GEONAME,POP,AGE"
    #datePred = "DATE_=7"
    forPred= "for=state:*"
    base_url = "https://api.census.gov/data/2017/pep/charage"
    endpoint = base_url+"?"+getString+","+getparam+"&"+forPred


    #param1 = {"get":request.form["parameters"]+request.form["parameters1"]+request.form["parameters2"], "for":"state:*"}
    return redirect(endpoint)






@app.route('/john')
def john():
    return 'John'

@app.route('/paul')
def paul():
    return 'Paul'

@app.route('/george')
def george():
    return 'George'

@app.route('/pip')
def pip():
    return render_template('pip.html', name='PIP')

@app.route('/flask')
def flasks():
    return render_template('flasks.html', name = 'Flask')

@app.route('/template')
def template():
    return render_template('template.html', name = 'Template')

@app.route('/route')
def route():
    return render_template('route.html', name = 'route')

@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_page.html", error=False)


    user = load_user(request.form["username"])
    if user is None:
        return render_template("login_page.html", error=True)

    if not user.check_password(request.form["password"]):
        return render_template("login_page.html", error=True)

    login_user(user)
    return redirect(url_for('landingpage'))


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required
def deletecomment(id):

    if request.method == "GET":
        return redirect(url_for('index'))

    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    flash('Item deleted')
    return redirect(url_for('index'))

@app.route("/addassignment", methods=["GET", "POST"])
@login_required
def addassignment():
    if request.method == "GET":
        return render_template("projectpractice.html", students = Students.query.all())

#Need to add grade

    assignment = Assignments(assignmentname=request.form["assignmentName"], classname=request.form["Class"], student_id=request.form["studentid"], grade=request.form["grade"])
    db.session.add(assignment)
    db.session.commit()
    flash("Assignment Added")
    return redirect(url_for('displayassignments'))

@app.route("/landing")
@login_required
def landingpage():
    return render_template('landingpage.html')

@app.route("/displayassignments")
@login_required
def displayassignments():
    return render_template("displayassignments.html", assignments=Assignments.query.all())


@app.route("/displaystudents")
@login_required
def displaystudents():
    return render_template("displaystudents.html", students=Students.query.all())

@app.route("/addstudent", methods=["GET", "POST"])
@login_required
def addstudent():
    if request.method == "GET":
        return render_template("addstudents.html")

    student = Students(fname=request.form["firstName"], lname=request.form["lastName"], major=request.form["Major"], email=request.form["email"])
    db.session.add(student)
    db.session.commit()
    flash("Student Added")
    return redirect(url_for("displaystudents"))

@app.route("/delete/assignment/<int:id>", methods=["GET", "POST"])
@login_required
def deleteassignment(id):

    if request.method == "GET":
        return redirect(url_for('displayassignments'))

    assignment = Assignments.query.get_or_404(id)
    db.session.delete(assignment)
    db.session.commit()
    flash('Item deleted')
    return redirect(url_for('displayassignments'))

@app.route("/delete/student/<int:id>", methods=["GET", "POST"])
@login_required
def deletestudent(id):

    if request.method == "GET":
        return redirect(url_for('displaystudents'))

    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Item deleted')
    return redirect(url_for('displaystudents'))

@app.route("/displayroster")
@login_required
def displayroster():
    return render_template("displayroster.html", students = db.session.query(Assignments).join(Students).order_by(Students.fname).all())

@app.route("/requestspecificstudent")
@login_required
def requeststudent():
    return render_template("requestspecificstudent.html", students = db.session.query(Students).all())


@app.route("/display/student", methods=["GET", "POST"])
@login_required
def displayspecificstudent():

    if request.method == "GET":
        return redirect(url_for('displayspecificstudent'))

    student = request.form["studentid"]
    result = db.session.query(Assignments).join(Students).order_by(Students.fname).filter(Assignments.student_id==student).all()
    return render_template("displayroster.html", students = result)

@app.route("/edit/grade/<int:id>", methods=["GET", "POST"])
@login_required
def editgrade(id):
    if request.method == "GET":
        return redirect(url_for('displayassignments'))

    student = Assignments.query.get_or_404(id)
    result = db.session.query(Assignments).join(Students).filter(Assignments.id==student.id).all()
    return render_template("editgrade.html", assignments = result)

@app.route("/updategrade/<int:id>", methods=["GET", "POST"])
@login_required
def updategrade(id):
    if request.method == "GET":
        return redirect(url_for('displayassignments'))

    newgrade = request.form["newGrade"]
    assignment = db.session.query(Assignments).get(id)
    assignment.grade = newgrade
    db.session.commit()
    return redirect(url_for('displayassignments'))

@app.route("/displayaveragegrades")
@login_required
def displayaverage():
    average = db.session.query(Students.fname, Students.lname, func.avg(Assignments.grade)).join(Students).group_by(Students.fname)
    return render_template('displayaveragegrade.html', averages = average)


result = db.session.query(Assignments).join(Students).filter(Assignments.id==27).all()
for row in result:
    print(row)
five = "hello"
getstring = "get="+five
print(getstring)

result1 = db.session.query(Students.fname, Students.lname, func.avg(Assignments.grade)).join(Students).group_by(Students.fname)
for row in result1:
    print(row[2])


