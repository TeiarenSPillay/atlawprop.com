import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imagine_property_investments.settings")

application = get_wsgi_application()
