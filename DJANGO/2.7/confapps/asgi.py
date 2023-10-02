"""
ASGI config for confapps project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'confapps.settings')

#application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application()
    }
)
