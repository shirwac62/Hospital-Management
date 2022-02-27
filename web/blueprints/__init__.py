from web.blueprints.dashboard.views import blueprint as dashbord
from web.blueprints.patient.views import blueprint as patient
from web.blueprints.nurse.views import blueprint as nurse
from web.blueprints.doctor.views import blueprint as doctor


tenant_list = [dashbord, patient, nurse, doctor]
