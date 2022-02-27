from flask import render_template

from utility.mkblueprint import ProjectBlueprint

blueprint = ProjectBlueprint('doctor', __name__)


@blueprint.route(blueprint.url, methods=['GET'])
def doctor():
    doctors = doctor.query.all()
    return render_template('doctor.html', title='doctor', doctors=doctors)



