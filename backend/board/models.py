from django.db import models


class PostVO(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:   # Meta 데이터클래스랑 연동하는 클래스
        managed = True
        db_table = 'posts'

    def __str__(self):
        return f'[{self.pk}] is username = {self.sequence},' \
               f' title = {self.title}'\
               f' content = {self.content}'\
               f' created_at = {self.created_at}'\
               f' updated_at = {self.updated_at}'