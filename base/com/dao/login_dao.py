from base import db
from base.com.vo.login_vo import LoginVO

class LoginDAO:
    def insert_login(self,login_vo):
        db.session.add(login_vo)
        db.session.commit()
