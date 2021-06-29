from rest_framework import serializers
from board.models import Post

class BoardSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()