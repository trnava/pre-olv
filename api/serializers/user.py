from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from api.models import (User, UserDetail)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = (
            'user_id',
            'icon',
            'ready_as_buyer',
            'last_name',
            'first_name',
            'zipcode',
            'address',
            'phone_number'
        )


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = (
            'user_id',
            'icon',
            'debuted',
            'approved',
            'ticket',
            'artist_name',
            'profile',
            'website',
            'sex',
            'place',
            'created_at',
            'updated_at'
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
