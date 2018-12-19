from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from api.models import (User, ArtistDetail, BuyerDetail)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerDetail
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistDetail
        fields = '__all__'


class ArtistInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistDetail
        fields = (
            'debuted',
            'approved',
            'ticket',
            'artist_name',
            'website',
            'birthday',
            'place',
            'profile',
            'icon',
            'user_id',
            'sex',
            'genre'
        )


class UserDetailSerializer(serializers.ModelSerializer):
    artist = SerializerMethodField()
    buyer = SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'email',
            'type',
            'artist',
            'buyer'
        )

    def get_artist(self, obj):
        artist = ArtistDetail.objects.filter(user_id=obj.pk).first()
        if artist is None:
            return False

        return ArtistSerializer(artist).data

    def get_buyer(self, obj):
        buyer = BuyerDetail.objects.filter(user_id=obj.pk).first()
        if buyer is None:
            return False

        return BuyerSerializer(buyer).data
