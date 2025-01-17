# chat/urls.py
from django.urls import path

# from . import views
from .views import MessageAPIView

# app_name = "chat"
urlpatterns = [
    # path("", views.index, name="index"),
    # path("<str:room_name>/", views.room, name="room"),
    path("messages", MessageAPIView.as_view()),
    path("messages/<int:user_id1>/<int:user_id2>/", MessageAPIView.as_view()),
]
