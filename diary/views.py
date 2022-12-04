from django.shortcuts import render,redirect
from diary.forms import diary_Form
from diary.models import Memory
from django.contrib import messages
# Create your views here.

def diaryindex(request):
    #전체 포스팅을 가져올 준비 , 아직 가져오지는 않음.
    diary_qs = Memory.objects.all().order_by("-id") #id필드에 대한 역순 정렬 (최신순)
    return render(request,"diary/d_index.html",{
        "diarypost_list": diary_qs
    })

def dsingle_post_page(request, pk): #request 모든 요구에 대한 정보
    d_post = Memory.objects.get(pk=pk)
    return render(request, "diary/d_single_post_page.html",{
        "diary_post":d_post,
    })

def diary_post_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == "GET":
        form = diary_Form(instance=memory)
    else:
        form = diary_Form(request.POST,instance=memory)
        if form.is_valid(): #유효성 검사 통과하면
            #유효성 거사에 통과한 값들이 저장된 dict
           # form.cleaned_data
           diarypost = form.save() #ModelForm에서 지원
           messages.success(request, "메모리를 생성했습니다.")
           #return redirect("/blog/")
           #return redirect(f"/blog/{post.pk}/")
           #return redirect(post.get_absolute_url()) 
           return redirect(diarypost)  #get~ 과 같은 의미

    return render(request, "diary/d_postform.html",{
        "form":form,
    })


def diary_edit(request, pk): #수정 기능
    memory = Memory.objects.get(pk=pk)
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == "GET":
        form = diary_Form(instance=memory)
    else:
        form = diary_Form(request.POST, instance=memory)
        if form.is_valid():  # 유효성 검사 통과하면
            # 유효성 거사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            diarypost = form.save() # ModelForm에서 지원
            messages.success(request,"메모리를 저장했습니다.")
            # return redirect("/blog/")
            # return redirect(f"/blog/{post.pk}/")
            # return redirect(post.get_absolute_url())
            return redirect(diarypost)  # get~ 과 같은 의미

    return render(request, "diary/d_postform.html", {
        "form": form,
    })

def memory_delete(request,pk):
    memory = Memory.objects.get(pk=pk)

    # Todo: delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "메모리를 삭제했습니다.")
        return redirect("/diary/")

    return render(request, "diary/memory_confirm_delete.html", {
        "memory": memory,
    })

