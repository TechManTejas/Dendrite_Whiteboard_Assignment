"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from . import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

websocket_urlpatterns = [
    re_path(r'/socket/', consumers.MyConsumer.as_asgi()),
    # Add more WebSocket consumers and paths as needed
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        websocket_urlpatterns
    ),
})