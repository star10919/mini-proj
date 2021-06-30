from django.db import models


class MemberVO(models.Model):     #상속,  #VO(Value Object)
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.EmailField()


    class Meta:   # Meta 데이터클래스랑 연동하는 클래스// 마리아db에서 테이블이 만들어짐
        managed = True
        db_table = 'members'

    def __str__(self):  #기계어를 자연어로 바꾸기 위함  (없어도됨)
        return f'[{self.pk}] {self.username}'