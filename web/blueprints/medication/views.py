from flask import render_template, flash, url_for, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.medication.forms import MedicationForm
from web.blueprints.medication.models import Medication
from web.extensions import save_to_db, delete, db

blueprint = ProjectBlueprint('medication', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_medication():
    form = MedicationForm()
    if form.validate_on_submit():
        data = Medication()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Medication has been created', 'success')
        return redirect(url_for('medication.medication'))
    return render_template('medication/add_medication.html', title='medication', form=form)

@blueprint.route(blueprint.url + "/edit/<medication_id>", methods=['GET', 'POST'])
def edit_medication(medication_id):
    data = Medication.query.get(medication_id)
    form = MedicationForm(obj=data)
    if form.validate_on_submit():
        data.code = form.code.data
        data.name = form.name.data
        data.brand = form.brand.data
        data.description = form.description.data
        save_to_db(data)
        flash('Your Medication has been Updated', 'success')
        return redirect(url_for('medication.medication'))
    return render_template('medication/edit.html', title='edit_medication', form=form, medication=Medication)


@blueprint.route(blueprint.url + "/delete/<medication_id>", methods=['GET', 'POST'])
def delete_medication(medication_id):
    data = Medication.query.get(medication_id)
    form = MedicationForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your Medication has been Deleted', 'success')
        return redirect(url_for('medication.medication'))
    return render_template('medication/delete.html', title="delete_medication", form=form, medication=Medication, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(medication.medication_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Medication.query.filter(Medication.code.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for n in data_list.items:
        row = [n.medication_id, n.code, n.name, n.brand, n.description,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"></i></a>'.format(
                   url_for('medication.edit_medication', medication_id=n.medication_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"></i></a>'.format(
                   url_for('medication.delete_medication', medication_id=n.medication_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})








@blueprint.route(blueprint.url, methods=['GET'])
def medication():
    Medications = Medication.query.all()
    return render_template('medication/medication.html', title='medication', Medications=Medications)

