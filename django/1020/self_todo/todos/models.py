from django.db import models
# 아래의 설정을 통해서 setting에 정의된 user의 model에 접근하여 외래키를 가져올 수 있다.
from django.conf import settings
# Create your models here.

class Todo(models.Model):
    title = models.TextField()
    completed = models.BooleanField()
    # 외래키 세팅즈의 user 모델을 사용하고 삭제 옵션은 참조 까지 다 삭제되는 cascade로 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)