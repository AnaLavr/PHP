from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome_page():
    return  render_template("index.html")  #buttons work login and registration

@app.route("/registration")      
def registration():
    return  render_template("registration.html")

@app.route ("/login")      #doesnt take to profile - why?
def login ():
    return render_template('login.html')

@app.route("/helper")   #settings button works
def helper():
    return  render_template("profilehelper.html")

@app.route("/helpee") #settings button works
def helpee():
    return  render_template("profilehelpeE.html")

@app.route("/switch")
def switch():
    return  render_template("switch.html")

@app.route("/needhelp")  #button works (form)
def needhelp():
    return  render_template("needhelpwith.html")

@app.route("/helpsubmit",methods=["POST"])     #only settings button works
def submit():
    data = request.form['selecthelp']
    return  render_template("nhw2.html", data=data)

@app.route("/regsubmit",methods=["POST"])
def regsubmit():
    data = request.form['category', 'category2']
    '''text = request.form['q','w','e']'''
    return  render_template("regsubmit.html", data=data)

 
    