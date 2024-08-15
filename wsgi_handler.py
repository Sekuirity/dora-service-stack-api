import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dora_metrics.settings')
application = get_wsgi_application()

from mangum import Mangum

handler = Mangum(application)
