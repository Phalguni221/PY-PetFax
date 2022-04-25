from flask import (Blueprint, render_template)

bp = Blueprint('main', __name__, url_prefix="/")


@bp.route('/')
def index():
<<<<<<< HEAD
    return render_template('pets/main.html')
=======
    return render_template('./pets/main.html')
>>>>>>> 4fc9f5bc5faba92b336938ebb798c77cb142f540
