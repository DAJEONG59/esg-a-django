from django.shortcuts import render,redirect
from blog.forms import PostForm,Restaurant_Form
from blog.models import Post, Restaurant
from django.views.generic import CreateView 

# 장고의 템플릿 시스템.order_by()

def index(request):
    #전체 포스팅을 가져올 준비 , 아직 가져오지는 않음.
    post_qs = Post.objects.all() #id필드에 대한 역순 정렬 (최신순)
    res_qs = Restaurant.objects.all()

    return render(request,"blog/index.html",{
        "post_list": post_qs,
        "restaurant_list": res_qs
    })

def single_post_page(request, pk): #request 모든 요구에 대한 정보
    post = Post.objects.get(pk=pk)


    return render(request, "blog/single_post_page.html",{
        "post":post,
    })

# post_new = CreateView.as_view(
#     form_class=PostForm,
#     model=Post,
#     success_url="/blog/",
# )

def post_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid(): #유효성 검사 통과하면
            #유효성 검사에 통과한 값들이 저장된 dict
           # form.cleaned_data
           post = form.save() #ModelForm에서 지원
           #return redirect("/blog/")
           #return redirect(f"/blog/{post.pk}/")
           #return redirect(post.get_absolute_url()) 



           return redirect(post)  #get~ 과 같은 의미


    return render(request, "blog/stt_last.html",{
        "form":form,
    })

#Restaurant


# def restaurant(request):
#     #전체 포스팅을 가져올 준비 , 아직 가져오지는 않음.
#     res_qs = Restaurant.objects.all().order_by("-id") #id필드에 대한 역순 정렬 (최신순)
#     return render(request,"blog/restaurant_index.html",{
#         "restaurant_list": res_qs
#     })


def r_post_page(request, pk): #request 모든 요구에 대한 정보
    res_post = Restaurant.objects.get(pk=pk)
    return render(request, "blog/r_page.html",{
        "r_post":res_post,
    })


def r_post_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == "GET":
        form = Restaurant_Form()
    else:
        form = Restaurant_Form(request.POST)
        if form.is_valid(): #유효성 검사 통과하면
            #유효성 거사에 통과한 값들이 저장된 dict
           # form.cleaned_data
           post = form.save() #ModelForm에서 지원
           #return redirect("/blog/")
           #return redirect(f"/blog/{post.pk}/")
           #return redirect(post.get_absolute_url()) 
           return redirect(post)  #get~ 과 같은 의미



    
    return render(request, "blog/r_postform.html",{
        "form":form,
    })