from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReadTextView.as_view(), name="read_text"),
]
