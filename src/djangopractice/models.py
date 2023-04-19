from django.db import models


# Create your models here.
class Question(models.Model):
    # 길이 제한 100
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    create_date = models.DateTimeField()


class Answer(models.Model):
    # 외래키 설정, 외래키의 참조가 삭제될시 이 로우도 같이 삭제되게 설정(CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    create_date = models.DateTimeField()