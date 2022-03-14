from flask import Flask, redirect, url_for, render_template, request, flash, jsonify
from utility.mkblueprint import ProjectBlueprint
from web.blueprints import doctor
from web.blueprints.department.forms import departmentForm
from web.blueprints.department.models import Department
from web.extensions import save_to_db, db

blueprint = ProjectBlueprint('department', __name__)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Department.appointment_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Department.query.filter(Department.department_name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for n in data_list.items:
        row = [n.department_id, n.department_name, n.Head_id, n.head_name,
               '<a href="{0}"><i class="fa fa-edit"style="color:green"></i></a>'.format(
                   url_for('department.edit_department', department_id=n.department_id)) + " " + \
               '<a href="{0}"><i class="fa fa-trash"style="color:red"></i></a>'.format(
                   url_for('department.delete_department', department_id=n.department_id))]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url + "/delete/<department_id>", methods=['GET', 'POST'])
def delete_department(department_id):
    data = Department.query.get(department_id)
    form = departmentForm(obj=data)
    if form.validate_on_submit():
        department(data)
        flash('Your department has been Deleted', 'success')
        return redirect(url_for('doctor.doctor'))
    return render_template('department/delete.html', title="delete_department", form=form, department=department,
                           data=data)


@blueprint.route(blueprint.url + "/edit/<department_id>", methods=['GET', 'POST'])
def edit_department(department_id):
    data = Department.query.get(department_id)
    form = departmentForm(obj=data)
    if form.validate_on_submit():
        data.department_id = form.department_id.data
        data.department_name = form.department_name.data
        data.Head_id = form.Head_id.data
        data.head_name = form.head_name.data
        save_to_db(data)
        flash('Your department has been Updated', 'success')
        return redirect(url_for('department.department'))
    return render_template('department/edit.html', title='edit_department', form=form, department=department, data=data)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_department():
    form = departmentForm()
    if form.validate_on_submit():
        data = Department()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Department has been created', 'success')
        return redirect(url_for('department.department'))
    return render_template('department/add.html', title='department', form=form)


@blueprint.route(blueprint.url, methods=['GET'])
def department():
    departments = Department.query.all()
    return render_template('department/department.html', title='department', departments=departments)
