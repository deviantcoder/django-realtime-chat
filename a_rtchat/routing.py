from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/chatroom/<chatroom_name>/', consumers.ChatroomConsumer.as_asgi())
]