from django.shortcuts import render
from django.views import View


class PassiveVoiceView(View):
    def get(self, request):
        return render(request, "passive_voice/index.html")
