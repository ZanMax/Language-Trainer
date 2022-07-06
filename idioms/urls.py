from django.urls import path
from . import views

urlpatterns = [
    path("", views.IdiomsView.as_view(), name="idioms"),
]
