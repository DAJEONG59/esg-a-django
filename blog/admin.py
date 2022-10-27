from django.contrib import admin
from blog.models import Post,Restaurant
# Register your models here.

admin.site.register(Post) # 모델을 admin에 등록
admin.site.register(Restaurant)
