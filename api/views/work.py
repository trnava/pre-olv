from rest_framework import viewsets

from api.models.work import Work
from api.serializers.work import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
