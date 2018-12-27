from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from api.models.user import User
from api.models.work import Work
from api.serializers.work import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    # queryset = Work.objects.all()
    serializer_class = WorkSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        artist_id = self.request.query_params.get('artist')
        if artist_id:
            works = Work.objects.filter(artist_id=artist_id).all()
            return works

        return Work.objects.all()

    def retrieve(self, request, pk=None):
        work = get_object_or_404(Work.objects.all(), pk=pk)

        work.view = work.view + 1
        work.save()

        return Response(WorkSerializer(work).data)

    def partial_update(self, request, pk=None):
        work = self.get_object()

        buyer_id = request.data.get('buyer', work.buyer)
        work.buyer = User.objects.filter(pk=buyer_id).first()
        work.sold = request.data.get('sold', work.sold)

        work.save()

        return Response(WorkSerializer(work).data)

