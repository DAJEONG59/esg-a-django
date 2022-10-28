from importlib.resources import path
from django.urls import path
from diary import views

urlpatterns = [
    path('',views.diaryindex),
    path('<int:pk>/',views.dsingle_post_page),
    path('new/',views.diary_post_new),
    path("<int:pk>/edit/", views.diary_edit),
    path("<int:pk>/delete/", views.memory_delete),

]