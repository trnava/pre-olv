from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from api.models.user import User
from api.models.work import Work
from api.models.favorite import Favorite
from api.serializers.work import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    # queryset = Work.objects.all()
    serializer_class = WorkSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        artist_id = self.request.query_params.get('artist')
        if artist_id:
            works = Work.objects.filter(artist=artist_id).all()
            return works

        user_id = self.request.query_params.get('favoritesOf')
        if user_id:
            works = []
            favorite_data = Favorite.objects.filter(user=user_id).all()
            for x in favorite_data:
                works.append(x.work)

            return works

        return Work.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data

        work = Work.objects.create(
            artist_id=data['artist'],
            name=data['name'],
            caption=data['caption'],
            image1=(data['image1'] == 'null') if None else data['image1'],
            price=data['price'],
            size_id=data['size'],
            color_id=data['color'],
            genre_id=data['genre'],
            subgenre_id=data['subgenre']
        )

        if data['image2'] != 'null':
            work.image2 = data['image2']

        if data['image3'] != 'null':
            work.image3 = data['image3']

        if data['image4'] != 'null':
            work.image4 = data['image4']

        if data['image5'] != 'null':
            work.image5 = data['image5']

        work.save()

        return Response(WorkSerializer(work).data)

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

