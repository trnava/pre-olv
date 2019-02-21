from django.http.response import HttpResponse

from api.views.user import *
from api.views.genre import *
from api.views.color import *
from api.views.size import *
from api.views.sex import *
from api.views.work import *
from api.views.image import *
from api.views.message import *
from api.views.favorite import *


def index(request):
    return HttpResponse('Connected')
