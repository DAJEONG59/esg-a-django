from importlib.resources import path
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index),
    path('<int:pk>/', views.single_post_page), #single_post_page 함수에 꼭 pk인자가 있어야한다. 
    path('new/', views.post_new),



    # path('restaurant/',views.restaurant),
    path('restaurant/<int:pk>/',views.r_post_page),
    path('restaurant/new/',views.r_post_new),
]