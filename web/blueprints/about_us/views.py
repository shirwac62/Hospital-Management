from flask import render_template

from utility.mkblueprint import ProjectBlueprint

blueprint = ProjectBlueprint('about_us', __name__)


@blueprint.route(blueprint.url, methods=['GET'])
def about_us():
    return render_template('about_us/about_us.html', title='about_us')
