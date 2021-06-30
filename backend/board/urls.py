from django.conf.urls import url
from .views import Boards as boards    #.하나만 있으면 바로 옆(sibling 관계)

urlpatterns = [
    url('/postwrite', boards.as_view())
]