from django.conf.urls import url
from member import views_fbv
from django.urls import path

urlpatterns = [     #프로젝트urls(leehaein.urls)랑 연결되는 부분
    url(r'^register', views_fbv.members),   #  시스템입장에서 여러사람들이 있는데에 추가되는 거니까 members
    url(r'^list', views_fbv.members),
    url(r'^modify', views_fbv.member_modify),
    url(r'^login', views_fbv.login),
    path('delete/<slug:pk>', views_fbv.member)  #slug:문자 / int:숫자
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