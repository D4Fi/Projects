import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'confapp.settings')

#application = get_asgi_application()

application = ProtocolTypeRouter(
        {
            "http": get_asgi_application(),
        }
)
