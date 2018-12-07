from rest_framework import viewsets

from api.models.size import Size
from api.serializers.size import SizeSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
