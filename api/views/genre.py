from rest_framework import viewsets

from api.models import (Genre, SubGenre)
from api.serializers import (GenreSerializer, SubGenreSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    """ genre """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class SubGenreViewSet(viewsets.ModelViewSet):
    """ sub genre"""
    queryset = SubGenre.objects.all()
    serializer_class = SubGenreSerializer
