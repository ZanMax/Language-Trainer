from django.db import models


class IrregularWords(models.Model):
    first_form = models.CharField(max_length=100, unique=True)
    second_form = models.CharField(max_length=100, unique=True)
    third_form = models.CharField(max_length=100, unique=True)
    translation = models.CharField(max_length=255)

    def __str__(self):
        return self.first_form

    class Meta:
        verbose_name_plural = "IrregularWords"
