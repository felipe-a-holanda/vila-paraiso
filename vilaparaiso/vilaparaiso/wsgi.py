"""
WSGI config for vilaparaiso project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vilaparaiso.settings")

# Activate your virtual env
activate_env=os.path.expanduser("~/vilaparaiso.org/env/bin/activate_this.py")
exec(open(activate_env).read(),dict(__file__=activate_env))

application = get_wsgi_application()
