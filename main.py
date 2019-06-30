from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/signup")
def display_signup_form():
    template = jinja_env.get_template("signup_form.html")
    return template.render()



@app.route("/signup", methods=["POST"])
def validate_signup():

    user_name = request.form["user_name"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    

    user_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    
    if not user_name:
        user_error = "That's not a valid username"
        user_name = ''
    else:
        if ' ' in user_name or len(user_name) < 3 or len(user_name) > 20:
            user_error = "That's not a valid username"
            user_name = ''


    if not password:
        password_error = "That's not a valid password"
        password = ''
    else:
        if ' ' in password or len(password) < 3 or len(password) > 20:
            password_error = "That's not a valid password"
            password = ''

    if not verify:
        verify_error = "Passwords don't match"
        verify = ''

    if not password == verify:
        verify_error = "Passwords don't match"
        password = ''
        verify = ''


    if not email:
        email = ""
    elif "@" and "." not in email:  
        email_error = "That's not a valid email"
        email = ''
    else:
        if ' ' in email or len(email) < 3 or len(email) > 20:
            email_error = "That's not a valid email"
            email = ''


    if not user_error and not password_error and not verify_error and not email_error:
        template = jinja_env.get_template("welcome_page.html")
        return template.render(user_name=user_name)
    else:
        template = jinja_env.get_template("signup_form.html")
        return template.render(user_error=user_error,
        password_error=password_error, verify_error=verify_error,
        user_name=user_name, password=password, verify=verify, email=email,
        email_error=email_error)

@app.route("/")
def index():
    template = jinja_env.get_template("signup_form.html")
    return template.render()

app.run()
