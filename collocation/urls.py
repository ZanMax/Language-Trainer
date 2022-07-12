from django.urls import path
from . import views

urlpatterns = [
    path("", views.TensesViews.as_view(), name="tenses"),
]