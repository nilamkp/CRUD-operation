from base import db

class LoginVO(db.Model):
    __tablename__ = 'login_table'
    login_id = db.Column('login_id', db.Integer, primary_key=True, autoincrement=True)
    email = db.Column('email', db.String(255), nullable=False)
    password = db.Column('password', db.Text, nullable=False)

db.create_all()

