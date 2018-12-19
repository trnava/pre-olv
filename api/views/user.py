from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import (User, ArtistDetail)
from api.serializers import (UserSerializer, UserDetailSerializer, ArtistInfoSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """ ユーザー """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    # permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        data = request.data

        user = User.objects.filter(email=data['email']).first()
        if user is None:
            user = User.objects.create_user(email=data['email'], password=data['password'])
            user.save()

            serialized_data = UserSerializer(user).data
            return Response(serialized_data)

        return Response({'message': '既に存在するユーザーです'}, status=404)

    def destroy(self, req, *args, **kwargs):
        pass


class ArtistViewSet(viewsets.ModelViewSet):
    """ アーティスト """
    queryset = ArtistDetail.objects.all()
    serializer_class = ArtistInfoSerializer

    def retrieve(self, request, pk=None):
        artist = get_object_or_404(ArtistDetail.objects.all(), user_id=pk)

        return Response(ArtistInfoSerializer(artist).data)
