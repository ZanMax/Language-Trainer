from django.shortcuts import render
from django.views import View


class ReadTextView(View):
    def get(self, request):
        return render(request, "read_text/index.html")
