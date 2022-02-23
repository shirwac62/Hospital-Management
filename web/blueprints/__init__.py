from web.blueprints.dashboard.views import blueprint as dashbord
from web.blueprints.patient.views import blueprint as patient
from web.blueprints.nurse.views import blueprint as nurse


tenant_list = [dashbord, patient, nurse]
