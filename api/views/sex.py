from rest_framework import viewsets

from api.models.sex import Sex
from api.serializers.sex import SexSerializer


class SexViewSet(viewsets.ModelViewSet):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer
