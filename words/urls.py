from django.urls import path
from . import views

urlpatterns = [
    path("", views.WordsView.as_view(), name="words"),
]
