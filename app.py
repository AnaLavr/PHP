import flask
from flask import Flask, render_template, request, url_for, abort, redirect
#from flask_login import LoginManager,   login_remembered,  login_user, login_required , current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
#from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import database
import os


from base64 import b64encode

UPLOAD_FOLDER = os.path.join('static')


app = Flask(__name__, template_folder="templates")
#auth = HTTPBasicAuth()
#login_manager = LoginManager()
#login_manager.init_app(app)

app.config['UPLOAD_FOLDER']='static'
app.config['SECRET_KEY'] = 'any secret string'

users = {
    "nastasja1493@yandex.ru": generate_password_hash("hello"),
    "igor@yandex.ru": generate_password_hash("hey"),
    "alex@mail.ru": generate_password_hash("hi")
}

hash = generate_password_hash('hello')
hash     #get the hash??

'''@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id) #What does it do?

class User():    
    
     def __init__(self, username):
         self.username=username
         
     def is_active(self):
        return True

    
     def is_authenticated(self):
        return self.authenticated

     def is_anonymous(self):
        return False
    
     def get_id(self):
        return self.email
    
     @classmethod
     def get(cls,username):
        return User(username)   #db what??

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')   
    
@app.route('/login', methods=['GET', 'POST'])

def login():
       
    form = LoginForm()
    if form.validate_on_submit():
        print('username', form.username.data)
       
        if   form.username.data in users and \
        check_password_hash(users.get(form.username.data), form.password.data):
     
   
         login_user(User)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        
        #if not is_safe_url(next):
         #   return flask.abort(400)

        return flask.redirect(next or member(ID))
    return flask.render_template('login.html', form=form)'''





@app.route("/")
def welcome_page():     # How to limit the tries for password?
    return  render_template("index.html")  


@app.route("/registration")      
def registration():
    return  render_template("registration.html")


@app.route("/member/<int:ID>") # how do i use login now????  /<int:helper_id> user=auth.current_user
#@login_required   
def member(ID):
    names=database.members(ID)
    
    return  render_template("memberprofile.html", names=names, ID=ID) 

@app.route('/inbox/<int:ID>')  #doesn't coordinate directly from members page /<int:ID>
def inbox(ID):
    messages=database.get_inbox_messages(ID)
    return render_template("inbox.html", messages=messages)



@app.route("/switch")
def switch():
    return  render_template("switch.html")

@app.route("/needhelp")  
def needhelp():
    return  render_template("needhelpwith.html")

@app.route("/helpsubmit",methods=["POST"])     
def submit():
    data = request.form['selecthelp']
    
    return  render_template("nhw2.html", data=data)

@app.route("/regsubmit",methods=["POST"])
def regsubmit():
    data =  []
    data.append (request.form['mode'])   #change the names and call the function
   # data.append (request.form.getlist('category2'))    DO NOT DELETE THIS LINE !!!find out how to delete ['']
    data.append (request.form['first_name'])
    data.append (request.form['city'])
    data.append (request.form['birth_date'])
    data.append (request.form['email'])
       #add phone num,age, last name
    photo = request.files['profile_photo']   
    content=photo.read()
    image= b64encode(content).decode("utf-8")
    return  render_template("regsubmit.html", data=data,photo=image)


@app.route("/helppost", methods=["POST"])
def helppost():
    data=[]
    data.append (request.form['category2'])
    data.append (request.form['problem'])
    data.append (request.form['time'])
    data.append (request.form['contact'])
    data.append (request.form['free'])
    pic = request.files['files']   
    content=pic.read()
    image= b64encode(content).decode("utf-8")
    
    return  render_template("helppost.html", data=data, photo=image)
 
#@app.route ('/logout')    #go back to login/registration page 
#def logout(): 
 #   return render_template("index.html"),401
 
@app.route('/logout')
#@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome_page'))
    
@app.route('/feed')
def feed():
    return render_template("feed.html")

