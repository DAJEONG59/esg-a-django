from django.core.validators import MaxValueValidator


from django.db import models


# Create your models here.

class Restaurant(models.Model):
    """맛집"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    average_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
        ])
    def get_absolute_url(self): #인자없는 함수, get_absolute_url은 장고에서 정해진 함수
        return f"/blog/restaurant/{self.pk}/"
    def __str__(self):
        return f"[{self.pk}] {self.name} "


# post model
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def get_absolute_url(self): #인자없는 함수, get_absolute_url은 장고에서 정해진 함수
        return f"/blog/{self.pk}/"
    # TO do : 향후에는 장고의 URL Reverse 기능을 사용하기.


    def __str__(self):
        return f"[{self.pk}] {self.title} "
        

    class Meta:
        # 퀘리셋에서 orderby를 지정하지 않았을 때 사용
        ordering = ['-id']





