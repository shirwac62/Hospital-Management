from flask import render_template, url_for, flash
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.prescribes.forms import PrescribesForm
from web.blueprints.prescribes.models import Prescribes
from web.extensions import save_to_db

blueprint = ProjectBlueprint('prescribes', __name__)

@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_prescribes():
    form = PrescribesForm()
    if form.validate_on_submit():
        data = Prescribes()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your prescribes has been created', 'success')
        return redirect(url_for('prescribes.prescribes'))
    for fieldName, errorMessages in form.errors.items():
        for err in errorMessages:
            print(fieldName, err)

    return render_template('prescribes/add.html', title='prescribes', form=form)


@blueprint.route(blueprint.url, methods=['GET'])
def prescribes():
    prescribes = Prescribes.query.all()
    return render_template('prescribes/prescribes.html', title='prescribes',prescribes=prescribes)


