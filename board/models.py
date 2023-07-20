from django.db import models

from common.models import Common
from django.contrib.auth.models import get_user_model

# Create your models here.


class Board(models.Model):
    objects = None
    title = models.CharField(max_length=64, verbose_name="글 제목")
    contents = models.TextField(verbose_name='글 내용')
    writer = models.ForeignKey('common.Common', on_delete=models.CASCADE, verbose_name='작성자')

    def __str__(self):
        return self.title

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.id = None
    #
    # def __str__(self):
    #     return 'id ={}, title={}'.format(self.id, self.title, self.contents)

    class Meta:
        db_table = "UserBoard"
        verbose_name = "Board"