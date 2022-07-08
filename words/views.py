import random

from django.shortcuts import render
from django.views import View

from .models import Words


class WordsView(View):
    def get(self, request):
        word_items = list(Words.objects.all())
        random_words = random.sample(word_items, 5)
        return render(request, 'words/index.html', {'words': random_words})
