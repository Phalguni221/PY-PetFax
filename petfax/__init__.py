# config                    
from flask import Flask

# factory
def create_app():
    app = Flask(__name__)


    
    # index route
    @app.route('/')
    def index(): 
        return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)

<<<<<<< HEAD
    from . import fact
    app.register_blueprint(fact.bp)
=======

    from . import fact
    app.register_blueprint(fact.bp)


>>>>>>> 4fc9f5bc5faba92b336938ebb798c77cb142f540

    # return the app 
    return app

