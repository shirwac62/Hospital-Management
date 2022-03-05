from flask import flash, url_for, render_template, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.procedure.form import ProcedureForm
from web.blueprints.procedure.models import Procedure
from web.extensions import save_to_db, delete, db

blueprint = ProjectBlueprint('procedure', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_procedure():
    form = ProcedureForm()
    if form.validate_on_submit():
        data = Procedure()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Procedure has been created', 'success')
        return redirect(url_for('procedure.procedure'))
    return render_template('procedure/add_procedure.html', title='procedure', form=form)




@blueprint.route(blueprint.url + "/edit/<procedure_id>", methods=['GET', 'POST'])
def edit_procedure(procedure_id):
    data = Procedure.query.get(procedure_id)
    form = ProcedureForm(obj=data)
    if form.validate_on_submit():
        data.cost_code = form.procedure_code.data
        data.procedure_name = form.procedure_name.data
        data.cost = form.cost.data
        save_to_db(data)
        flash('Your Procedure has been Updated', 'success')
        return redirect(url_for('procedure.procedure'))
    return render_template('procedure/edit.html', title='edit_procedure', form=form, procedure=procedure)


@blueprint.route(blueprint.url + "/delete/<procedure_id>", methods=['GET', 'POST'])
def delete_procedure(procedure_id):
    data = Procedure.query.get(procedure_id)
    form = ProcedureForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your procedure has been Deleted', 'success')
        return redirect(url_for('nurse.nurse'))
    return render_template('procedure/delete.html', title="delete_procedure", form=form, procedure=procedure, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Procedure.procedure_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Procedure.query.filter(Procedure.procedure_code.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for n in data_list.items:
        row = [n.procedure_id, n.procedure_code, n.procedure_name, n.cost,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"></i></a>'.format(
                   url_for('procedure.dit_procedure', procedure_id=n.procedure_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"></i></a>'.format(
                   url_for('procedure.delete_procedure', procedure_id=n.procedure_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def procedure():
    Procedures= Procedure.query.all()
    return render_template('pocedure/pocedure.html', title='pocedure', Procedures=Procedures)
