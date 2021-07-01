from django.conf.urls import url
from member import views_fbv

urlpatterns = [     #프로젝트urls(leehaein.urls)랑 연결되는 부분
    url(r'^register', views_fbv.members),   #url(r'^ ~~') : 정규식 사용
    url(r'^list', views_fbv.members)
]

'''
CBV 방식 (Class Based View)
from django.conf.urls import url
from .views import Members as members
from .views import Member as member
from django.urls import path, include
urlpatterns = [
    url('/register', members.as_view()),
    path('/<int:pk>/', member.as_view()),
]
'''