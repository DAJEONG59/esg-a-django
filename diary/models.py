from django.db import models

# Create your models here.
class Memory(models.Model):
    """일기"""
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self): #인자없는 함수, get_absolute_url은 장고에서 정해진 함수
        return f"/diary/{self.pk}/"
    def __str__(self):
        return f"[{self.pk}] {self.title}"

