from flask import flash, render_template, url_for, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.doctor.forms import DoctorForm
from web.blueprints.doctor.models import Doctor
from web.extensions import save_to_db, delete, db

blueprint = ProjectBlueprint('doctor', __name__)


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


@blueprint.route(blueprint.url + "/edit/<doc_id>", methods=['GET', 'POST'])
def edit_doctor(doc_id):
    data = Doctor.query.get(doc_id)
    form = DoctorForm(obj=data)
    if form.validate_on_submit():
        data.doc_full_name = form.doc_full_name.data
        data.doc_address = form.doc_address.data
        data.doc_ph_no = form.doc_ph_no.data
        save_to_db(data)
        flash('Your Doctor has been Updated', 'success')
        return redirect(url_for('doctor.doctor'))
    return render_template('doctor/edit.html', title='edit_doctor', form=form, doctor=Doctor)


@blueprint.route(blueprint.url + "/delete/<doc_id>", methods=['GET', 'POST'])
def delete_doctor(doc_id):
    data = Doctor.query.get(doc_id)
    form = DoctorForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your Doctor has been Deleted', 'success')
        return redirect(url_for('doctor.doctor'))
    return render_template('doctor/delete.html', title="delete_doctor", form=form, doctor=Doctor, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Doctor.doc_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Doctor.query.filter(Doctor.doc_full_name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.doc_id, b.doc_full_name, b.doc_address,  b.doc_ph_no,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"style="color:green"></i></a>'.format(
                   url_for('doctor.edit_doctor', doc_id=b.doc_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"style="color:red"></i></a>'.format(
                   url_for('doctor.delete_doctor', doc_id=b.doc_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def doctor():
    Doctors = Doctor.query.all()
    return render_template('doctor/doctor.html', title='doctor', Doctors=Doctors)
