from flask import render_template, flash, url_for, request, jsonify
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints.room.forms import RoomForm
from web.blueprints.room.models import Room
from web.extensions import save_to_db, delete, db

blueprint = ProjectBlueprint('room', __name__)


@blueprint.route(blueprint.url + "/add", methods=['GET', 'POST'])
def add_room():
    form = RoomForm()
    if form.validate_on_submit():
        data = Room()
        form.populate_obj(data)
        save_to_db(data)
        flash('Your Room has been created', 'success')
        return redirect(url_for('room.room'))
    return render_template('room/add.html', title='room', form=form)


@blueprint.route(blueprint.url + "/edit/<room_id>", methods=['GET', 'POST'])
def edit_room(room_id):
    data = Room.query.get(room_id)
    form = RoomForm(obj=data)
    if form.validate_on_submit():
        data.room_no = form.room_no.data
        data.room_type = form.room_type.data
        data.available = form.available.data
        save_to_db(data)
        flash('Your Room has been Updated', 'success')
        return redirect(url_for('room.room'))
    return render_template('room/edit.html', title='edit_room', form=form, room=Room)


@blueprint.route(blueprint.url + "/delete/<room_id>", methods=['GET', 'POST'])
def delete_room(room_id):
    data = Room.query.get(room_id)
    form = RoomForm(obj=data)
    if form.validate_on_submit():
        delete(data)
        flash('Your Room has been Deleted', 'success')
        return redirect(url_for('patient.patient'))
    return render_template('room/delete.html', title="delete_room", form=form, room=Room, data=data)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(Room.room_id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = Room.query.filter(Room.room_type.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.room_id, b.room_no, b.room_type, b.available,
               '<a href="{0}"><i class="fa-solid fa-pen-to-square"style="color:green"></i></a>'.format(
                   url_for('room.edit_room', room_id=b.room_id)) + " " + \
               '<a href="{0}"><i class="fa-solid fa-trash"style="color:red"></i></a>'.format(
                   url_for('room.delete_room', room_id=b.room_id))
               ]

        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


@blueprint.route(blueprint.url, methods=['GET'])
def room():
    Rooms = Room.query.all()
    return render_template('room/room.html', title='room', Rooms=Rooms)
