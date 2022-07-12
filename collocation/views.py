from django.shortcuts import render

from django.views import View


class Collocation(View):
    def get(self, request):
        return render(request, "collocation/index.html")
