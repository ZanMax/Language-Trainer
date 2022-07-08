from django.shortcuts import render
from django.views import View
from .models import ReadText
import random


class ReadTextView(View):
    def get(self, request):
        items = list(ReadText.objects.all())
        random_text = random.choice(items)
        return render(request, "read_text/index.html", {"text": random_text})
