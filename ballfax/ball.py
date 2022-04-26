from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import (Blueprint, render_template, redirect, request)

def create_app():
    app = Flask(__name__)

# factory 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Phalguni2025@localhost:5432/ballfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False             

#register model blueprint
    from . import ballmodels 
    ballmodels.db.Ball(app) 
    migrate = Migrate(app, ballmodels.db)

bp = Blueprint('ball', __name__, url_prefix="/ball")
    
    # index route
    @app.route('/ballfax')
    def ballindex(): 
            return 'Hello, BallFax!'
    

    # # register pet blueprint 
    # from . import pet
    # app.register_blueprint(pet.bp)

    # #register fact blueprint
    # from . import fact
    # app.register_blueprint(fact.bp)
