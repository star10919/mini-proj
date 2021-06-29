from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.models import Member
from member.serializers import MemberSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic

class Auth(APIView):
    def get(self, request):
        ic(request)
        print('########## 저장 1 ##########')
        serializer = MemberSerializers(data=request)
        if serializer.is_valid():
            print('########## 저장 2 ##########')
            serializer.save()
        return Response({'result': 'WELCOME'})


@csrf_exempt
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Member.objects.all()
        serializer = MemberSerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializers(data=data)
        if serializer.is_valid():   #유효성 체크
            serializer.save()       #저장
            return JsonResponse(serializer.data, status=201)   #serializer을 data로 바꿔줌
        return JsonResponse(serializer.errors, status=400)