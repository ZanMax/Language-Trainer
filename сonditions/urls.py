from django.urls import path
from . import views

urlpatterns = [
    path("", views.ConditionsView.as_view(), name="conditions"),
]
