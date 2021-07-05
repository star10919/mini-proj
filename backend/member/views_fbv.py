from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from member.models import MemberVO
from member.serializers import MemberSerializers
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
from django.http import HttpResponse
from rest_framework import serializers
import json

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

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def member(request):
    if request.method == 'GET':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = MemberVO.objects.get(pk=pk)
        if member is not None:
            ic(member)
            if user_input_password == member.password:
                serializer = MemberSerializers(member, many=False)
                ic(type(serializer.data))
                return JsonResponse(data=serializer.data, safe=False)
            else:
                print('비밀번호가 다릅니다.')
                return JsonResponse(data=[{'result':'PASSWORD-FAIL'}], status=201)
        else:
            print('해당 아이디가 없음')
            return JsonResponse(data=[{'result':'USERNAME-FAIL'}], status=201)

        return HttpResponse(status=104)
    elif request.method == 'PUT':
        data = request.data['body']
        update_member = data['member']
        ic(update_member)
        pk = update_member['username']
        member = MemberVO.objects.get(pk=pk)
        user_change_password = update_member['password']
        ic(user_change_password)
        serializer = MemberSerializers(member, data= data['member'], partial=True)  #partial=True 써야 일시적X, 계속 저장됨
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result':f'Update Success , {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)