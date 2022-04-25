from flask import ( Blueprint, render_template ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/')
def new(): 
    return render_template('facts/index.html')
<<<<<<< HEAD
=======

>>>>>>> 4fc9f5bc5faba92b336938ebb798c77cb142f540
