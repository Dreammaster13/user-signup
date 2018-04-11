from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template('signup_page.html') 

@app.route("/validate", methods=["POST"])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error_check = False
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if " " in username or username == " ":
        username_error = "Enter valid username."
        error_check = True
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username has invalid length!"
        error_check = True
    if " " in password or password == "":
        password_error = "Invalid password."
        password = ""
        verify = ""
        error_check = True
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password has invalid length!"
        password = ""
        verify = ""
        error_check = True
    if password != verify:
        verify_error = "Passwords do not match!"
        password = ""
        verify = ""
        error_check = True
    elif verify == "":
        verify_error = "Passwords do not match!"
        error_check = True
    if email != "":
        if email.count('@') !=1:
            email_error = "Please enter vavid email address."
            error_check = True
        if email.count(".") !=1:
            email_error = "Please enter valid email address."
            error_check = True
        if " " in email:
            email_error = "Please enter valid email address."
            error_check = True
    if error_check == True:
        return render_template('signup_page.html', username_error=username_error,
            password_error=password_error, verify_error=verify_error,
            email_error=email_error, username=username, password=password,
            verify=verify, email=email)
    else:
        return render_template('welcome_page.html', username=username)

app.run()