

from flask import *


app = Flask(__name__)

from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db


# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    #app.run(debug=True) # run the flask app on debug mode

@main.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  

    return render_template("success.html", name = f.filename)  
  
if __name__ == '__main__':  

   app.run(port=5000, debug=True)
