from django.db import models


# https://www.ef.com/wwen/english-resources/english-idioms/
# https://www.theidioms.com/

class Idioms(models.Model):
    idiom = models.CharField(max_length=100, unique=True)
    meaning = models.CharField(max_length=100, unique=True)
    example = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.idiom

    class Meta:
        verbose_name_plural = "Idioms"
