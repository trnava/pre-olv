from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# import for media root
from django.conf import settings
from django.conf.urls.static import static

from api.views.custom_auth_token import CustomAuthToken

from api.views import (
    UserViewSet,
    UserDetailViewSet,
    ArtistViewSet,
    GenreViewSet,
    SubGenreViewSet,
    ColorViewSet,
    SizeViewSet,
    SexViewSet,
    WorkViewSet,
    MessageViewSet,
    FavoriteViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'userDetails', UserDetailViewSet, base_name='user_detail')
router.register(r'artists', ArtistViewSet, base_name='artist')
router.register(r'genres', GenreViewSet, base_name='genre')
router.register(r'sub_genres', SubGenreViewSet, base_name='sub_genre')
router.register(r'colors', ColorViewSet, base_name='color')
router.register(r'sizes', SizeViewSet, base_name='size')
router.register(r'sexs', SexViewSet, base_name='sex')
router.register(r'works', WorkViewSet, base_name='work')
router.register(r'messages', MessageViewSet, base_name='message')
router.register(r'favorites', FavoriteViewSet, base_name='favorite')

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # Api
    path('api/v1/', include(router.urls)),

    # login api
    path('api-token-auth/', CustomAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
