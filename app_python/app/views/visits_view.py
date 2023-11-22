from flask import Blueprint,render_template

visits_blueprint = Blueprint('visits', __name__)

@visits_blueprint.route("/visits")
def visits():
    with open('visits', 'r') as f:
        data = f.read()
    return render_template('visits.html', visits=data)
