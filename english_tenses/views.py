from django.shortcuts import render
from django.views import View


class TensesViews(View):
    def get(self, request):
        return render(request, "english_tenses/index.html")
