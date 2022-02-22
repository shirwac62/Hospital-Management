from flask import render_template

from utility import blueprint
from utility.mkblueprint import ProjectBlueprint

blueprint = ProjectBlueprint('/', __name__)


@blueprint.route(blueprint.url, methods=['GET'])
def dashboard():
    return render_template('index.html', title='dashboard')
