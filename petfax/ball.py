from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import (Blueprint, render_template, redirect, request)

def create_app():
    app = Flask(__name__)

# factory 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Phalguni2025@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

#register model blueprint
    from . import ballmodels 
    ballmodels.db.Ball(app) 
    migrate = Migrate(app, ballmodels.db)

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/ball', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = ballmodels.Fact(submitter=submitter, fact=fact)
        ballmodels.db.session.add(new_fact)
        ballmodels.db.session.commit()

        return redirect('/facts')
    
    results = ballmodels.Fact.query.all()
    for result in results:
       print(results)

    return render_template('facts/index.html', facts=results)

@bp.route('/new')
def new(): 
    return render_template('facts/new.html')
