from flask import render_template, redirect, url_for, flash
from app.auth.views import logged_in_user
from .shoppinglist_form import ShoppingList

from . import home

@home.route('/')
def homepage():
    
   # Render the homepage template on the / route

    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
def dashboard():

    #check if user is logged in
    if logged_in_user == None:
        flash("You must be logged in to access this page")
        return redirect( url_for('auth.login'))
    
    form = ShoppingList()
    if form.validate_on_submit():
        #insert to list
        pass

        #
    
    #Render the dashboard template on the /dashboard route    
    return render_template('home/dashboard.html',form=form, title="Dashboard")