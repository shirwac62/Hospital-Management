from flask import render_template, url_for, flash, jsonify, request
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.doctor.forms import DoctorForm
from web.blueprints.doctor.models import Doctor
from web.extensions import save_to_db, db, delete

blueprint = ProjectBlueprint('doctor', __name__)


@blueprint.route(blueprint.url + "/edit/<doctor_id>", methods=['GET', 'POST'])
def edit_doctor(doctor_id):
    data = Doctor.query.get(doctor_id)
    form = DoctorForm(obj=data)
    if form.validate_on_submit():
        data.doctor_first_name = form.doctor_first_name.data
        data.doctor_last_name = form.doctor_last_name.data
        data.doctor_address = form.doctor_address.data
        data.doctor_ph_no = form.doctor_ph_no.data
        save_to_db(data)
        flash('Your doctor has been Updated', 'success')
        return redirect(url_for('doctor.doctor'))
    return render_template('doctor/edit.html', title='edit_doctor', form=form, doctor=doctor, data=data)


@blueprint.route(blueprint.url + "/delete/<doctor_id>", methods=['GET', 'POST'])
def delete_doctor(doctor_id):
    data = Doctor.query.get(doctor_id)
    form = DoctorForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your doctor has been Deleted', 'success')
        return redirect(url_for('doctor.doctor'))
    return render_template('doctor/delete.html', title="delete_doctor", form=form, doctor=doctor, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    print("pub_index  pub_index")
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Doctor.doctor_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Doctor.query.filter(Doctor.doctor_first_name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.doctor_id, b.doctor_first_name, b.doctor_last_name, b.doctor_address, b.doctor_ph_no,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"></i></a>'.format(
                   url_for('doctor.edit_doctor', doctor_id=b.doctor_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"></i></a>'.format(
                   url_for('doctor.delete_doctor', doctor_id=b.doctor_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})



@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_doctor():
    form = DoctorForm()
    if form.validate_on_submit():
        data = Doctor()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Doctor has been created', 'success')
        return redirect(url_for('doctor.doctor'))
    return render_template('doctor/add.html', title='doctor', form=form)


@blueprint.route(blueprint.url, methods=['GET'])
def doctor():
    Doctors = Doctor.query.all()
    return render_template('doctor/doctor.html', title='doctor', Doctors=Doctors)
