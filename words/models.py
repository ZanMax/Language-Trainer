from django.db import models


class Words(models.Model):
    word = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
    example = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name_plural = "Words"
