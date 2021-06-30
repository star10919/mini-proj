from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from board.models import PostVO as post
from board.serializers import BoardSerializers



class Boards(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = BoardSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Success, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)

class Board(APIView):
    def get(self, request):
        pass


@csrf_exempt
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = post.objects.all()
        serializer = BoardSerializers(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializers(data=data)
        if serializer.is_valid():   #유효성 체크
            serializer.save()       #저장
            return JsonResponse(serializer.data, status=201)   #serializer을 data로 바꿔줌
        return JsonResponse(serializer.errors, status=400)
