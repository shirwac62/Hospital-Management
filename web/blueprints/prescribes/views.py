from flask import render_template, flash, url_for, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.prescribes.forms import PrescribesForm
from web.blueprints.prescribes.models import Prescribes
from web.extensions import save_to_db, delete, db

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


@blueprint.route(blueprint.url + "/edit/<prescribes_id>", methods=['GET', 'POST'])
def edit_prescribes(prescribes_id):
    data = Prescribes.query.get(prescribes_id)
    form = PrescribesForm(obj=data)
    if form.validate_on_submit():
        data.doc_full_name = form.doc_full_name.data
        data.pat_full_name = form.pat_full_name.data
        data.med_code = form.med_code.data
        data.appointment_name = form.appointment_name.data
        data.date = form.date.data
        data.dose = form.dose.data
        save_to_db(data)
        flash('Your prescribes has been Updated', 'success')
        return redirect(url_for('prescribes.prescribes'))
    return render_template('prescribes/edit.html', title='edit_prescribes', form=form, prescribes=prescribes)


@blueprint.route(blueprint.url + "/delete/<prescribes_id>", methods=['GET', 'POST'])
def delete_prescribes(prescribes_id):
    data = Prescribes.query.get(prescribes_id)
    form = PrescribesForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your prescribes has been Deleted', 'success')
        return redirect(url_for('prescribes.prescribes'))
    return render_template('prescribes/delete.html', title="delete_prescribes", form=form, prescribes=prescribes,
                           data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Prescribes.prescribes_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Prescribes.query.filter(Prescribes.doc_full_name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.prescribes_id, b.doc_full_name, b.pat_full_name, b.med_code, b.date, b.appointment_name, b.dose,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"style="color:green"></i></a>'.format(
                   url_for('prescribes.edit_prescribes', prescribes_id=b.prescribes_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"style="color:red"></i></a>'.format(
                   url_for('prescribes.delete_prescribes', prescribes_id=b.prescribes_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def prescribes():
    Prescribe = Prescribes.query.all()
    return render_template('prescribes/prescribes.html', title='prescribes', Prescribe=Prescribe)
