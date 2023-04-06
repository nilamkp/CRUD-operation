from flask import *
from base import app
from base.com.vo.register_vo import RegisterVO
from base.com.dao.register_dao import RegisterDAO


@app.route('/admin/insert_register',methods=["POST"])
def insert_register():
    first_name=request.form.get('firstname')
    last_name=request.form.get('lastname')
    email=request.form.get('email')
    password=request.form.get('password')

    register_vo = RegisterVO()
    register_dao = RegisterDAO()

    register_vo.first_name = first_name
    register_vo.last_name = last_name
    register_vo.email = email
    register_vo.password = password

    register_dao.insert_register(register_vo)

    return render_template('admin/login.html')