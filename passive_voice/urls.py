from django.urls import path
from . import views

urlpatterns = [
    path("", views.PassiveVoiceView.as_view(), name="passive_voice"),
]
