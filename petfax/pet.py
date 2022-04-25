<<<<<<< HEAD
=======

>>>>>>> 4fc9f5bc5faba92b336938ebb798c77cb142f540
import json
from flask import (Blueprint, render_template)

bp = Blueprint('pet', __name__, url_prefix="/pets")


pets = json.load(open('pets.json'))
# print(pets)


@bp.route('/')
def index():
<<<<<<< HEAD
    return render_template('pets/index.html', pets=pets)
=======
    return render_template('./pets/index.html', pets=pets)

>>>>>>> 4fc9f5bc5faba92b336938ebb798c77cb142f540
