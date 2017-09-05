from flask import render_template, redirect, url_for, flash, session
from app.shoppingcart import ShoppingCart
from .shoppinglist_form import ShoppingList

from . import home

shopping_lists = {}

#method to remove item from the cart
def removeItem(item_name):

    if isinstance( item_name, str):
        pass
    else:
        raise ValueError

#a method to calculate total cost
def calculatePrice(price, quantity):        
    total_amount = price * quantity
    return total_amount

def addToDic(key, value):    
    shopping_lists.setdefault(key, [])
    shopping_lists[key].append(value)

############# routes or endpoints ################################

@home.route('/')
def homepage():
    
   # Render the homepage template on the / route

    return render_template('home/index.html', title="Welcome")

@home.route('/add-new', methods=['POST', 'GET'])
def newlist():

    #check if user is logged in
    # if not session["logged_in"]:
    #     flash("You must be logged in to access this page")
    #     return redirect( url_for('auth.login'))
    
    form = ShoppingList()
    if form.validate_on_submit():
        #insert to list
        item_id = len( shopping_lists ) + 1        
        shopping_list = ShoppingCart(session["email"], form.title.data, form.price.data, 
                                        form.quantity.data, item_id, form.description.data)
        addToDic(session["email"], shopping_list)
        result = shopping_lists
        flash("List saved okay")
        return render_template('home/dashboard.html', title="Dashboard", result = result)

    #Render the dashboard template on the /dashboard route    
    return render_template('home/newlist.html',form=form, title="Add new")

@home.route('/dashboard')
def dashboard():
    # if session["logged_in"] == True:        
    #     return render_template("home/dashboard.html" )
    #else:
    #flash("You must be logged in to access this page")
    #return redirect(url_for('auth.login') )
    return render_template("home/dashboard.html" )
