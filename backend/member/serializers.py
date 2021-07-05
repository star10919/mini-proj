from rest_framework import serializers
from member.models import MemberVO as member
from icecream import ic


class MemberSerializers(serializers.Serializer):   #rest라서 Serializer해야 됨.
    # pk인 id는 99퍼센트 수정 안 할 것이므로 read_only
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    class Meta:
        model = member
        fields = '__all__'

    def create(self, validated_data):
        return member.objects.create(**validated_data)  # **는 딕셔너리 형태

    def update(self, instance, validated_data):
        member.objects.filter(pk=instance.username).update(**validated_data)
        return member