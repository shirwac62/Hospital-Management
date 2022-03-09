from flask import render_template, url_for, flash
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.appointment.forms import AppointmentForm
from web.blueprints.appointment.models import Appointment
from web.extensions import save_to_db

blueprint = ProjectBlueprint('appointment', __name__)


@blueprint.route(blueprint.url + "/edit/<appointment_id>", methods=['GET', 'POST'])
def edit_appointment(appointment_id):
    data = Appointment.query.get(appointment_id)
    form = AppointmentForm(obj=data)
    if form.validate_on_submit():
        data.patient_name = form.patient_name.data
        data.Appointment_name = form.Appointment_name.data
        data.Appointment_Date = form.Appointment_Date.data
        save_to_db(data)
        flash('Your appointment has been Updated', 'success')
        return redirect(url_for('patient.patient'))
    return render_template('appointment/edit.html', title='edit_appointment', form=form, appointment=appointment)


@blueprint.route(blueprint.url + "/delete/<appointment_id>", methods=['GET', 'POST'])
def delete_appointment(appointment_id):
    data = Appointment.query.get(appointment_id)
    form = AppointmentForm(obj=data)
    if form.validate_on_submit():
        Appointment(data)
        flash('Your appointment has been Deleted', 'success')
        return redirect(url_for('appointment.appointment'))
    return render_template('appointment/delete.html', title="delete_appointment", form=form, appointment=appointment, data=data)



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