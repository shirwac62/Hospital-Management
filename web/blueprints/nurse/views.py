from flask import render_template, flash, url_for, request, jsonify
from werkzeug.utils import redirect
from utility.mkblueprint import ProjectBlueprint
from web.blueprints.nurse.forms import NurseForm
from web.blueprints.nurse.models import Nurse
from web.extensions import save_to_db, db, delete

blueprint = ProjectBlueprint('nurse', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_nurse():
    form = NurseForm()
    if form.validate_on_submit():
        data = Nurse()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your nurse has been created', 'success')
        return redirect(url_for('nurse.nurse'))
    return render_template('nurse/add_medication.html', title='nurse', form=form)




@blueprint.route(blueprint.url + "/edit/<nurse_id>", methods=['GET', 'POST'])
def edit_nurse(nurse_id):
    data = Nurse.query.get(nurse_id)
    form = NurseForm(obj=data)
    if form.validate_on_submit():
        data.nurse_first_name = form.nurse_first_name.data
        data.nurse_last_name = form.nurse_last_name.data
        data.nurse_address = form.nurse_address.data
        data.nurse_ph_no = form.nurse_ph_no.data
        save_to_db(data)
        flash('Your Nurse has been Updated', 'success')
        return redirect(url_for('nurse.nurse'))
    return render_template('nurse/edit.html', title='edit_nurse', form=form, nurse=Nurse)


@blueprint.route(blueprint.url + "/delete/<nurse_id>", methods=['GET', 'POST'])
def delete_nurse(nurse_id):
    data = Nurse.query.get(nurse_id)
    form = NurseForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your nurse has been Deleted', 'success')
        return redirect(url_for('nurse.nurse'))
    return render_template('nurse/delete.html', title="delete_nurse", form=form, nurse=Nurse, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    print("pub_index  pub_index")
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Nurse.nurse_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Nurse.query.filter(Nurse.nurse_first_name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for n in data_list.items:
        row = [n.nurse_id, n.nurse_first_name, n.nurse_last_name, n.nurse_address, n.nurse_ph_no,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"></i></a>'.format(
                   url_for('nurse.edit_nurse', nurse_id=n.nurse_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"></i></a>'.format(
                   url_for('nurse.delete_nurse', nurse_id=n.nurse_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def nurse():
    Nurses = Nurse.query.all()
    return render_template('nurse/nurse.html', title='nurse', Nurses=Nurses)
