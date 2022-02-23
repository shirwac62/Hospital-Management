from flask import render_template

from utility.mkblueprint import ProjectBlueprint

blueprint = ProjectBlueprint('nurse', __name__)


@blueprint.route(blueprint.url, methods=['GET'])
def nurse():
    return render_template('nurse.html', title='nurse')
