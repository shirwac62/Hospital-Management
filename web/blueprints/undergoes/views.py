from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from utility.mkblueprint import ProjectBlueprint
from web.blueprints import undergoes
from web.blueprints.undergoes.forms import UndergoesForm
from web.blueprints.undergoes.models import Undergoes
from web.extensions import save_to_db

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




@blueprint.route(blueprint.url, methods=['GET'])
def room():
    undergo = Undergoes.query.all()
    return render_template('undergoes/undergoes.html', title='undergoes',undergo=undergo)
