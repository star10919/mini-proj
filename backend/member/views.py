from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.

from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.models import MemberVO as member
from member.serializers import MemberSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic


class Members(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = MemberSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'WELCOME, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)


class Member(APIView):
    def get_object(self, pk):
        try:
            return member.objects.get(pk=pk)
        except member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        login = self.get_object(pk)
        serializer = MemberSerializers(login)
        return Response({'result': f'WELCOME'})


@csrf_exempt
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = member.objects.all()
        serializer = MemberSerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializers(data=data)
        if serializer.is_valid():   #유효성 체크
            serializer.save()       #저장
            return JsonResponse(serializer.data, status=201)   #serializer을 data로 바꿔줌
        return JsonResponse(serializer.errors, status=400)

