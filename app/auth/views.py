from app.user import User
from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm

users = {}
logged_in_user = None


@auth.route("/register", methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add a user to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=form.password.data)
        

        # add new user to list        
        
        users[logged_in_user] = user

        #alert user to login
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template if error occured
    return render_template('auth/register.html', form=form, title='Register')

@auth.route("/login", methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data in users.keys(): #email is correct
            user_account = users[ form.email.data ]

            #check if password exists
            if user_account.password == form.password.data:
                logged_in_user = form.email.data
                return redirect( url_for('home.dashboard'))
            
            flash("Sorry, password or email incorrect")
            #redirect to the login page
            return redirect(url_for('auth.login'))

        flash("Sorry, password or email incorrect")
        #redirect to the login page
        return redirect(url_for('auth.login'))

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route("/logout")
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log a user out through the logout link
    """
    logged_in_user = None
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))