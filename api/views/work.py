from rest_framework import viewsets

from api.models.work import Work
from api.serializers.work import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    # queryset = Work.objects.all()
    serializer_class = WorkSerializer

    def get_queryset(self):
        artist_id = self.request.query_params.get('artist')
        if artist_id:
            works = Work.objects.filter(artist_id=artist_id).all()
            return works

        return Work.objects.all()
