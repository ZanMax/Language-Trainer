from django.shortcuts import render
from django.views import View


class ConditionsView(View):

    def get(self, request):
        return render(request, "conditions/index.html")
