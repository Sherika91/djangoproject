from django.db import models


class Material(models.Model):
    title = models.CharField(max_length=200, verbose_name="Name")
    body = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"
