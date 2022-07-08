from django.db import models


class ReadText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "ReadText"
