from web.blueprints.dashboard.views import blueprint as dashbord
from web.blueprints.patient.views import blueprint as patient
from web.blueprints.nurse.views import blueprint as nurse
from web.blueprints.doctor.views import blueprint as doctor
from web.blueprints.appointment.views import blueprint as appointment
from web.blueprints.department.views import blueprint as department
from web.blueprints.medication.views import blueprint as medication
from web.blueprints.procedure.views import blueprint as procedure
from web.blueprints.room.views import blueprint as room
from web.blueprints.undergoes.views import blueprint as undergoes
from web.blueprints.prescribes.views import blueprint as prescribes
from web.blueprints.about_us.views import blueprint as about_us

tenant_list = [dashbord, patient, nurse, doctor, appointment, department, medication, procedure, room, undergoes,prescribes,about_us]
