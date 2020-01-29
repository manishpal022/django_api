import os

# from dj_static import Cling

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

# application = Cling(get_wsgi_application())
application = get_wsgi_application()
