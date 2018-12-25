from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from api.models.user import (User, ArtistDetail, BuyerDetail)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        email = request.data['username']
        user = User.objects.filter(email=email).first()
        if user is None:
            return Response({'message': '存在しないユーザーです'}, status=404)

        serializer = self.serializer_class(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        artist = ArtistDetail.objects.filter(user_id=user.pk).exists()
        buyer = BuyerDetail.objects.filter(user_id=user.pk).exists()

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'artist': artist,
            'buyer': buyer
        })
