from django.contrib import admin
from .models import Words

# Register your models here.

admin.site.register(Words)

admin.site.site_header = "Language Trainer Admin"
admin.site.site_title = "Language Trainer Admin"
admin.site.index_title = "Welcome to Language Trainer"
