from base import db

class RegisterVO(db.Model):
    __tablename__ = 'register_table'
    register_id = db.Column('register_id',db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column('first_name',db.String(255),nullable=False)
    last_name = db.Column('last_name',db.String(255),nullable=False)
    email = db.Column('email',db.String(255), nullable=False)
    password = db.Column('password',db.Text, nullable=False)

db.create_all()
