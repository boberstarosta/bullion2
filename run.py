import os
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

    application = get_wsgi_application()
    call_command('runserver',  'localhost:8080', '--noreload')
