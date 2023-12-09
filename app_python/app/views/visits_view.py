from flask import Blueprint,render_template
import os

visits_blueprint = Blueprint('visits', __name__)

VISITSFILE = os.environ.get("VISITFILE", "./visits")

@visits_blueprint.route("/visits")
def visits():
    with open(VISITSFILE, 'r') as f:
        data = f.read()
    return render_template('visits.html', visits=data)
