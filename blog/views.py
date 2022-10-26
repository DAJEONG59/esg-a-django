from django.shortcuts import render

# 장고의 템플릿 시스템

def index(request):
    return render(request,"blog/index.html")