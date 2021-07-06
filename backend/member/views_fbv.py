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
import datetime

now = datetime.datetime.now()
@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):       # 전체
    if request.method == 'GET':     # header에 전부 담아 이동
        all_members = MemberVO.objects.all()        # 1. 모델 객체 가져오기
        # print(f'***{type(all_members)}***')       # all_member의 타입 : Queryset
        serializer = MemberSerializers(all_members, many=True)   #  2.모델에 있는 객체를 시리얼라이저 해서 DB로 보내고
        # print(f'***{type(serializer)}***')      # serializer의 타입 : ListSerializer
        return JsonResponse(serializer.data, safe=False)   # 3. DB에 있는 serializer.data(Json임)를 JsonResponse라는 컨테이너에 담아 리액트로 이동  #safe=False : 무상태(저장x)
    elif request.method == 'POST':      # body에 담아 은닉화(보안유지 가능)
        new_member = request.data['body']
        ic(new_member)
        serializer = MemberSerializers(data=new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'DELETE'])  # 같은 패밀리끼리 묶어주기(REST 방식이라서!!)
def member(request, pk):
    try:    # try~except return 까지 없어도 무방(단, 화면단에서는 삭제됐느데, DB에서 삭제됐는지 확인할 때-오류추적할 때 유용)
        print(f'------ {now.strftime("%Y-%m-%d %H:%M:%S")} ------')
        member = MemberVO.objects.filter(username=pk)
        if member is not None:
            ic(member)
        else:
            print('member is None')
    except MemberVO.DoesNotExist:
        return JsonResponse({'result': 'MEMBER-NOT-EXISTS'}, status=201)

    if request.method == 'GET':
        serializer = MemberSerializers()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        MemberVO.objects.get(username=pk).delete()
        return JsonResponse({'result': 'Deleted Complete'}, status=201)

@api_view(['PUT'])
def member_modify(request):
    data = request.data['body']
    update_member = data['member']
    ic(update_member)
    pk = update_member['username']
    member = MemberVO.objects.get(pk=pk)
    user_change_password = update_member['password']
    ic(user_change_password)
    serializer = MemberSerializers(member, data=data['member'], partial=True)   #partial=True는 수정된 부분 저장이라는 뜻
    if serializer.is_valid():
        serializer.save()   # 덮어쓰기가 아니라 수정된 부분만 저장
        return JsonResponse({'result': f'Update Success , {serializer.data.get("name")}'}, status=201)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = MemberVO.objects.get(pk=pk)
        ic(member)
        if user_input_password == member.password:
            serializer = MemberSerializers(member, many=False)
            ic(type(serializer.data))
            return JsonResponse(data=serializer.data, safe=False)
        else:
            print('비밀번호가 다릅니다.')
            return JsonResponse({'result': 'PASSWORD-FAIL'}, status=201)
    except MemberVO.DoesNotExist:
        return JsonResponse({'result': 'USERNAME-FAIL'}, status=201)


    return HttpResponse(status=104)