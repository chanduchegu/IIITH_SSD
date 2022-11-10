import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager,login_manager,login_user,logout_user,login_required,UserMixin)
from sqlalchemy.sql import func 

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"]="12122121"
db = SQLAlchemy(app)

login_manager=LoginManager()
login_manager.init_app(app)
class User(UserMixin,db.Model):
    
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Student {self.name}>'
    def get_id(self):
        return self.email
@app.route('/user/signin',methods=['POST'])
def signin():
    if(request.method=='POST'):
        req=request.get_json()
        email=req['email']
        password=req['password']
        check_user=User.query.filter_by(email=email).first()
        # print(check_user)
        if(check_user is not None):
            if(check_user.password==password):
                login_user(check_user)
                return "LOGGED in successfully"
            else:
                return "Incorrect password"
        else:
            return "No such User exists"
@app.route('/user/signup',methods=['POST'])
def signup():
    if(request.method=='POST'):
        req=request.get_json()
        name=req['name']
        email=req['email']
        password=req['password']
        check_user=User.query.filter_by(email=email).first()
        if(check_user is None):
                db.session.add(User(name=name,email=email,password=password))   
                db.session.commit()
                return "SignUp successfully"
        else:
                return "User already present"
# @app.route('/user/logout',methods=['POST'])
# @login_required
# def logout():
#     if(request.method=='POST'):
#         req=request.get_json()
#         logout_user()
#         return "Logout successfully"
#     else:
#         return "User already present"
    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port="5000",debug=True)
