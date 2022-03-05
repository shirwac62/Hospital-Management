from web.blueprints.dashboard.views import blueprint as dashbord
from web.blueprints.patient.views import blueprint as patient
from web.blueprints.nurse.views import blueprint as nurse
from web.blueprints.doctor.views import blueprint as doctor
from web.blueprints.appointment.views import blueprint as appointment
from web.blueprints.department.views import blueprint as department


tenant_list = [dashbord, patient, nurse, doctor, appointment, department]
