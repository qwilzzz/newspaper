from django.urls import path
from .views import PostNList, PostNDetail, Posts, Search  # импортируем наше представление

urlpatterns = [
    # path -- означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', PostNList.as_view()),
    path('<int:pk>/', PostNDetail.as_view()),
    path('posts/', Posts.as_view()),
    path('search/', Search.as_view()),
]