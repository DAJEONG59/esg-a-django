from importlib.resources import path
from django.urls import path
from blog import views

urlpatterns = [
    path('blog/',views.index),
    path('blog/<int:pk>/', views.single_post_page), #single_post_page 함수에 꼭 pk인자가 있어야한다. 
    path('new/', views.post_new),
]