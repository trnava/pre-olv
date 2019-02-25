from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from api.models.work import Work
from api.models.size import Size
from api.models.color import Color
from api.models.genre import Genre, SubGenre
from api.models.user import UserDetail
from api.models.favorite import Favorite
from api.serializers.user import ArtistSerializer, BuyerSerializer
from api.serializers.size import SizeSerializer
from api.serializers.color import ColorSerializer
from api.serializers.genre import GenreSerializer, SubGenreSerializer


class WorkSerializer(serializers.ModelSerializer):
    size = SerializerMethodField()
    color = SerializerMethodField()
    genre = SerializerMethodField()
    subgenre = SerializerMethodField()
    buyer = SerializerMethodField()
    artist = SerializerMethodField()
    favorite_users = SerializerMethodField()

    class Meta:
        model = Work
        fields = (
            'id',
            'view',
            'status',
            'name',
            'caption',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'price',
            'sold',
            'created_at',
            'updated_at',
            'size',
            'color',
            'genre',
            'subgenre',
            'buyer',
            'artist',
            'favorite_users'
        )

    def get_size(self, obj):
        return SizeSerializer(Size.objects.get(pk=obj.size.pk)).data

    def get_color(self, obj):
        return ColorSerializer(Color.objects.get(pk=obj.color.pk)).data

    def get_genre(self, obj):
        return GenreSerializer(Genre.objects.get(pk=obj.genre.pk)).data

    def get_subgenre(self, obj):
        return SubGenreSerializer(SubGenre.objects.get(pk=obj.subgenre.pk)).data

    def get_buyer(self, obj):
        if obj.buyer is None:
            return {}

        return BuyerSerializer(UserDetail.objects.get(user_id=obj.buyer)).data

    def get_artist(self, obj):
        return ArtistSerializer(UserDetail.objects.get(user_id=obj.artist)).data

    def get_favorite_users(self, obj):
        user_ids = []
        data = Favorite.objects.filter(work=obj.pk).all()

        for i in data:
            user_ids.append(i.user_id)

        return user_ids
