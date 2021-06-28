from django.db import models


class Member(models.Model):     #상속
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()


    class Meta:   # Meta 데이터클래스랑 연동하는 클래스
        managed = True
        db_table = 'members'