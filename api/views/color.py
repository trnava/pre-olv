from rest_framework import viewsets

from api.models.color import Color
from api.serializers.color import ColorSerializer


class ColorViewSet(viewsets.ModelViewSet):
    """ color """
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

