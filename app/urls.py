from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views.custom_auth_token import CustomAuthToken

from api.views import (
    UserViewSet,
    ArtistViewSet,
    GenreViewSet,
    SubGenreViewSet,
    ColorViewSet,
    SizeViewSet,
    SexViewSet,
    WorkViewSet,
    ImageViewSet,
    MessageViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'artists', ArtistViewSet, base_name='artist')
router.register(r'genres', GenreViewSet, base_name='genre')
router.register(r'sub_genres', SubGenreViewSet, base_name='sub_genre')
router.register(r'colors', ColorViewSet, base_name='color')
router.register(r'sizes', SizeViewSet, base_name='size')
router.register(r'sexs', SexViewSet, base_name='sex')
router.register(r'works', WorkViewSet, base_name='work')
router.register(r'images', ImageViewSet, base_name='image')
router.register(r'messages', MessageViewSet, base_name='message')

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Api
    path('api/v1/', include(router.urls)),

    # login api
    path('api-token-auth/', CustomAuthToken.as_view()),
]
