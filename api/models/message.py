from django.db import models

from api.models.work import Work
from api.models.user import *


class Message(models.Model):
    work = models.ForeignKey(Work, on_delete=models.PROTECT)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.PROTECT)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.PROTECT)
    body = models.TextField(null=False, blank=False)
