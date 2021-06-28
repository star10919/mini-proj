from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:   # Meta 데이터클래스랑 연동하는 클래스
        managed = True
        db_table = 'posts'