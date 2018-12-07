from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class SubGenre(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name
