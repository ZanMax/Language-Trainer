from django.shortcuts import render

from django.views import View
from .models import Words


class WordsView(View):
    def get(self, request):
        words = Words.objects.all()
        return render(request, 'words/index.html', {'words': words})
