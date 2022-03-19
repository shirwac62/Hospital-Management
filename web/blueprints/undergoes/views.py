from flask import render_template, flash, url_for, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints import undergoes
from web.blueprints.room.models import Room
from web.blueprints.undergoes.forms import UndergoesForm
from web.blueprints.undergoes.models import Undergoes
from web.extensions import save_to_db, delete, db

blueprint = ProjectBlueprint('undergoes', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_undergoes():
    form = UndergoesForm()
    if form.validate_on_submit():
        data = Undergoes()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your undergoes has been created', 'success')
        return redirect(url_for('undergoes.undergoes'))
    return render_template('undergoes/add_undergoes.html', title='undergoes', form=form)


@blueprint.route(blueprint.url + "/edit/<undergoes_id>", methods=['GET', 'POST'])
def edit_undergoes(undergoes_id):
    data = Undergoes.query.get(undergoes_id)
    form = UndergoesForm(obj=data)
    if form.validate_on_submit():
        data.doc_full_name = form.doc_full_name.data
        data.pat_full_name = form.pat_full_name.data
        data.procedure_code = form.procedure_code.data
        data.date = form.date.data
        data.name = form.name.data
        data.room_no = form.room_no.data
        save_to_db(data)
        flash('Your Undergoes has been Updated', 'success')
        return redirect(url_for('undergoes.undergoes'))
    return render_template('undergoes/edit.html', title='edit_undergoes', form=form, undergoes=Undergoes)


@blueprint.route(blueprint.url + "/delete/<undergoes_id>", methods=['GET', 'POST'])
def delete_undergoes(undergoes_id):
    data = Undergoes.query.get(undergoes_id)
    form = UndergoesForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your Room has been Deleted', 'success')
        return redirect(url_for('undergoes.undergoes'))
    return render_template('undergoes/delete.html', title="delete_undergoes", form=form, undergoes=Undergoes, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Undergoes.undergoes_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Undergoes.query.filter(Undergoes.doc_full_name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.undergoes_id, b.doc_full_name, b.pat_full_name, b.procedure_code, b.date, b.name, b.room_no,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"></i></a>'.format(
                   url_for('undergoes.edit_undergoes', undergoes_id=b.undergoes_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"></i></a>'.format(
                   url_for('undergoes.delete_undergoes', undergoes_id=b.undergoes_id))
               ]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def undergoes():
    undergoes = Undergoes.query.all()
    return render_template('undergoes/undergoes.html', title='undergoes', undergoes=undergoes)
