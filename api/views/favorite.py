from rest_framework import viewsets

from api.models.favorite import Favorite
from api.serializers.favorite import FavoriteSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """ favorite """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

