from flask import render_template, flash, url_for, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.appointment.forms import AppointmentForm
from web.blueprints.appointment.models import Appointment
from web.extensions import save_to_db, delete, db

blueprint = ProjectBlueprint('appointment', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        data = Appointment()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Appointment has been created', 'success')
        return redirect(url_for('appointment.appointment'))
    for fieldName, errorMessages in form.errors.items():
        for err in errorMessages:
            print(fieldName, err)


    # do something with your errorMessages for fieldName
    return render_template('appointment/add.html', title='appointment', form=form)


@blueprint.route(blueprint.url + "/edit/<appointment_id>", methods=['GET', 'POST'])
def edit_appointment(appointment_id):
    data = Appointment.query.get(appointment_id)
    form = AppointmentForm(obj=data)
    if form.validate_on_submit():
        data.doctor_name = form.doctor_name.data
        data.patient = form.patient.data
        save_to_db(data)
        flash('Your appointment has been Updated', 'success')
        return redirect(url_for('appointment.appointment'))
    return render_template('appointment/edit.html', title='edit_appointment', form=form, doctor=Appointment)


@blueprint.route(blueprint.url + "/delete/<appointment_id>", methods=['GET', 'POST'])
def delete_appointment(appointment_id):
    data = Appointment.query.get(appointment_id)
    form = AppointmentForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your appointment has been Deleted', 'success')
        return redirect(url_for('appointment.appointment'))
    return render_template('appointment/delete.html', title="delete_appointment", form=form, doctor=Appointment,
                           data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Appointment.appointment_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Appointment.query.filter(Appointment.appointment_name.ilike('%' + search + '%')).paginate(page, length,
                                                                                                          True)
    data = []
    for b in data_list.items:
        row = [b.appointment_id, b.appointment_name, b.doctor_name, b.patient_name, b.date,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"style="color:green"></i></a>'.format(
                   url_for('appointment.edit_appointment', appointment_id=b.appointment_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"style="color:red"></i></a>'.format(
                   url_for('appointment.delete_appointment', appointment_id=b.appointment_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def appointment():
    Appointments = Appointment.query.all()
    return render_template('appointment/appointment.html', title='appointment', Appointments=Appointments)
