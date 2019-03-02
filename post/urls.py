from django.urls import path
from .views import PostLV, PostDV, PostCreate

app_name = 'post'
urlpatterns = [
    path('',PostLV.as_view(), name="home"),
    path('<int:pk>/',PostLV.as_view(), name="category"),
    path('post/<int:pk>/',PostDV.as_view(), name="detail"),
    path('post/create/',PostCreate.as_view(),name="create"),
]
