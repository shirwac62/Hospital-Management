from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.patient.forms import PatientForm
from web.blueprints.patient.models import Patient
from web.extensions import save_to_db

blueprint = ProjectBlueprint('patient', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_patient():
    form = PatientForm()
    if form.validate_on_submit():
        data = Patient()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Patient has been created', 'success')
        return redirect(url_for('patient.patient'))
    return render_template('add.html', title='patient', form=form)


@blueprint.route(blueprint.url, methods=['GET'])
def patient():
    Patients = Patient.query.all()
    return render_template('patient.html', title='patient', Patients=Patients)
