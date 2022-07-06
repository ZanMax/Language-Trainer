from django.urls import path
from . import views

urlpatterns = [
    path("", views.IrregularVerbsView.as_view(), name="irregular_verbs"),
]
