from flask import render_template, flash, url_for, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.patient.forms import PatientForm
from web.blueprints.patient.models import Patient
from web.extensions import save_to_db, db, delete

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
    return render_template('patient/add.html', title='patient', form=form)


@blueprint.route(blueprint.url + "/edit/<patient_id>", methods=['GET', 'POST'])
def edit_patient(patient_id):
    data = Patient.query.get(patient_id)
    form = PatientForm(obj=data)
    if form.validate_on_submit():
        data.pat_full_name = form.pat_full_name.data
        data.pat_address = form.pat_address.data
        data.pat_insurance_no = form.pat_insurance_no.data
        data.pat_ph_no = form.pat_ph_no.data
        save_to_db(data)
        flash('Your Patient has been Updated', 'success')
        return redirect(url_for('patient.patient'))
    return render_template('patient/edit.html', title='edit_patient', form=form, patient=Patient)


@blueprint.route(blueprint.url + "/delete/<patient_id>", methods=['GET', 'POST'])
def delete_patient(patient_id):
    data = Patient.query.get(patient_id)
    form = PatientForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your Patient has been Deleted', 'success')
        return redirect(url_for('patient.patient'))
    return render_template('patient/delete.html', title="delete_patient", form=form, patient=Patient, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Patient.patient_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Patient.query.filter(Patient.pat_full_name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.patient_id, b.pat_full_name, b.pat_address,  b.pat_insurance_no,b.pat_ph_no,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"style="color:green"></i></a>'.format(
                   url_for('patient.edit_patient', patient_id=b.patient_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"style="color:red"></i></a>'.format(
                   url_for('patient.delete_patient', patient_id=b.patient_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def patient():
    Patients = Patient.query.all()
    return render_template('patient/patient.html', title='patient', Patients=Patients)
