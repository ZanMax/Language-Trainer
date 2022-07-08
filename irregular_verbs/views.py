from django.shortcuts import render

from django.views import View
from .models import IrregularWords


class IrregularVerbsView(View):
    def get(self, request):
        irregular_verbs = IrregularWords.objects.all()
        return render(request, "irregular_verbs/index.html", {"irregular_verbs": irregular_verbs})
