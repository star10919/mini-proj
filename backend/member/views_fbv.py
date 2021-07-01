from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from member.models import MemberVO
from member.serializers import MemberSerializers
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
from rest_framework import serializers

@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):       # 전체
    if request.method == 'GET':     # header에 전부 담아 이동
        all_members = MemberVO.objects.all()
        # print(f'***{type(all_members)}***')       # all_member의 타입 : Queryset
        serializer = MemberSerializers(all_members, many=True)
        # print(f'***{type(serializer)}***')      # serializer의 타입 : ListSerializer
        return JsonResponse(serializer.data, safe=False)      #safe=False : 무상태(저장x)
    elif request.method == 'POST':      # body에 담아 은닉화(보안유지 가능)
        new_member = request.data['body']
        ic(new_member)
        serializer = MemberSerializers(data=new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def member(request, pk):        # 한개, 사용안함
    if request.method == 'GET':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)