from django.conf.urls import url
from django.urls import path
from .views import Members as members  # .하나만 있으면 바로 옆(sibling 관계)
from .views import Member as member
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [     #리액트랑 연결되는 부분
    url('/signup', members.as_view()),
    path('/login/<str:pk>/', member.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)