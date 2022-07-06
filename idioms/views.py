from django.shortcuts import render
from django.views import View


class IdiomsView(View):
    def get(self, request):
        return render(request, "idioms/index.html")
