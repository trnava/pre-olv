from rest_framework import viewsets
from rest_framework.response import Response

from api.models.favorite import Favorite
from api.serializers.favorite import FavoriteSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """ favorite """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        favorite = Favorite.objects.filter(work=data['work'], user=data['user']).first()
        if favorite:
            favorite.delete()
            return Response(status=200)

        favorite = Favorite.objects.create(work_id=data['work'], user_id=data['user'])
        favorite.save()

        return Response(FavoriteSerializer(favorite).data)
