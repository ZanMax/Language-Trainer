from django.urls import path
from . import views

urlpatterns = [
    path("", views.WordsView.as_view(), name="irregular_verbs"),
]
