from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    #모델 변경시 makemigrations와 migrate를 통해 데이터베이스를 변경해 주어야한다.
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=models.CASCADE는 계정이 삭제되면 이 계정이 작성한 질문을 모드 삭제하라는 의미이다.

    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    #모델 변경시 makemigrations와 migrate를 통해 데이터베이스를 변경해 주어야한다. python manage.py makemigrations python manage.py migrate
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
