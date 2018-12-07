from django.db import models
from django.utils.timezone import now

from api.models.size import Size
from api.models.color import Color
from api.models.genre import *
from api.models.user import User


class Work(models.Model):
    view = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    name = models.CharField(max_length=30,null=False, blank=False)
    caption = models.TextField(null=False, blank=False)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    subgenre = models.ForeignKey(SubGenre, on_delete=models.PROTECT)
    price = models.IntegerField(default=0, null=False, blank=False)
    sold = models.BooleanField(default=False)
    buyer = models.ForeignKey(User, related_name='buyer', null=True, blank=True, on_delete=models.PROTECT)
    artist = models.ForeignKey(User, related_name='artist', null=True, blank=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
