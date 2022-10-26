from django.shortcuts import render
from blog.models import Post

# 장고의 템플릿 시스템

def index(request):
    #전체 포스팅을 가져올 준비 , 아직 가져오지는 않음.
    post_qs = Post.objects.all().order_by("-id") #id필드에 대한 역순 정렬 (최신순)
    return render(request,"blog/index.html",{
        "post_list": post_qs
    })

