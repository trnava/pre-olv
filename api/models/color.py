from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=10)
    color_code = models.CharField(max_length=10)
