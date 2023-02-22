# This is a sample Python script.
from flask import Flask, render_template , request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import pymysql
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app= Flask(__name__)
app.secret_key="Secret Key"

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:@localhost/crud"
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False


db=SQLAlchemy(app)
db.init_app(app)
class Employee(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email=db.Column(db.String(80))

    def __init__(self,name,email):
        self.name=name
        self.email=email




@app.route("/")
def home():
    all_Data=Employee.query.all()
    return render_template("index.html", employee=all_Data)

@app.route("/insert", methods=["POST"])
def insert():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']

        myData=Employee(name,email)
        db.session.add(myData)
        db.session.commit()
        flash("Employee has been added successfully!")

        return redirect(url_for("home"))


@app.route("/update", methods=["GET","POST"])
def update():
    if request.method=="POST":
        my_Data=Employee.query.get(request.form.get('id'))

        my_Data.name=request.form['name']
        my_Data.email=request.form['email']

        db.session.commit()
        flash("Employee Updated Successfully!")

        return redirect(url_for("home"))


@app.route("/delete/<id>",methods=["GET","POST"])
def delete(id):
    my_data=Employee.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully!")

    return redirect(url_for("home"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
    # with app.app_context():
    #     db.create_all()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
