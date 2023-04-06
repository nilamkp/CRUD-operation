from flask import *
from base import app
from base.com.dao.login_dao import LoginDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.register_vo import RegisterVO

@app.route('/')
def home():
    return render_template('admin/login.html')

@app.route('/admin/register')
def register():
    return render_template('admin/register.html')

@app.route('/admin/load_login', methods=["POST"])
def load_login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = RegisterVO.query.filter_by(email=email).filter_by(password=password).first()
        print("bhsknfkshfesafvnkjvhyiuhfhirjenfnjoaef", user)
        if user is None:
            flash("Invalid User Name Or Pssword ")
            return redirect("/")
        else:
            return render_template('home.html')
    return redirect('/admin/load_login')
