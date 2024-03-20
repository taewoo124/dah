from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField('제목', max_length=100)
    description = models.TextField('설명')
    body = models.TextField('본문')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
