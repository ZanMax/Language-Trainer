from django.shortcuts import render
from django.views import View
from .models import Idioms


class IdiomsView(View):
    def get(self, request):
        idioms = Idioms.objects.all()
        return render(request, "idioms/index.html", {"idioms": idioms})
