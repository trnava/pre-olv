from django.db import models
from api.models.work import Work
from api.models.user import User


class Favorite(models.Model):
    work = models.ForeignKey(Work, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
