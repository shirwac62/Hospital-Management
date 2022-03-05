from flask import render_template, url_for, flash
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.appointment.forms import AppointmentForm
from web.extensions import save_to_db

blueprint = ProjectBlueprint('appointment', __name__)



@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        data = appointment()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your appointment has been created', 'success')
        return redirect(url_for('appointment.appointment'))
    return render_template('appointment/add.html', title='appointment', form=form)




@blueprint.route(blueprint.url, methods=['GET'])
def appointment():
    # appointments = appointment.query.all()
    return render_template('appointment/appointment.html', title='appointment')