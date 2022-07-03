from django.shortcuts import render

from django.views import View


class IrregularVerbsView(View):
    def get(self, request):
        return render(request, "irregular_verbs/index.html")
