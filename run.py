from flask import Flask, render_template, request, flash
from app.forms import SignIn, UserRegistrationForm, AdminRegistration

app = Flask(__name__ ,template_folder='Designs')

#set up secret key for crsf
app.secret_key = "M@0$"

#route users to home page
@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

#route user to registration or signup form
@app.route("/signup", methods = ["GET", "POST"])
def signup():
    form = UserRegistrationForm()
    if request.method == "GET":
        return render_template("signup.html", form=form)
    elif request.method == "POST":
        if form.validate_on_submit():
            if "user exists":
                return "Email taken"
            else:
                return "create our user here"
        else:
            return "form didnt validate"


#this will be after user is logged in
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin")
def adminSign():
    return render_template("admin.html")


#redirect admin to signup page if he is not signed up
@app.route("/admin/signup")
def adminSignup():
    return render_template("admin_signup.html")

@app.route("/resetpassword")
def passwdReset():
    return render_template("pass_reset.html")

@app.route("/admin/resetpassword")
def adminPasswdReset():
    return render_template("pass_reset.html")


#run the app

if __name__ == "__main__":
    #app.run( debug=True,host='0.0.0.0' )
    app.run(debug=True)