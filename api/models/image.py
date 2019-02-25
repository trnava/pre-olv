from django.db import models

from api.models.work import Work


class Image(models.Model):
    work = models.ForeignKey(Work, on_delete=models.PROTECT)
    order = models.IntegerField()
    url = models.ImageField(null=False, blank=True, upload_to='workImages/')
