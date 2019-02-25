from django.db import models
from django.utils.timezone import now

from api.models.size import Size
from api.models.color import Color
from api.models.genre import *
from api.models.user import User


class Work(models.Model):
    view = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    name = models.CharField(null=False, blank=False, max_length=100,)
    caption = models.TextField(null=False, blank=False)
    image1 = models.ImageField(null=False, blank=True, upload_to='workImages/')
    image2 = models.ImageField(default=None, null=True, blank=True, upload_to='workImages/')
    image3 = models.ImageField(default=None, null=True, blank=True, upload_to='workImages/')
    image4 = models.ImageField(default=None, null=True, blank=True, upload_to='workImages/')
    image5 = models.ImageField(default=None, null=True, blank=True, upload_to='workImages/')
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    subgenre = models.ForeignKey(SubGenre, on_delete=models.PROTECT)
    price = models.IntegerField(default=0, null=False, blank=False)
    sold = models.BooleanField(default=False)
    buyer = models.ForeignKey(User, related_name='buyer', null=True, blank=True, on_delete=models.PROTECT)
    artist = models.ForeignKey(User, related_name='artist', null=False, default=0, blank=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)
    deleted_at = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
