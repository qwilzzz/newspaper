from django.urls import path
from .views import PostNList, Search, PostDetail, PostCreate, PostDelete, PostUpdate  # импортируем наше представление

app_name = 'news'
urlpatterns = [
    # path -- означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', PostNList.as_view()),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/create', PostCreate.as_view(), name='post_create'),
    path('search/', Search.as_view(), name='search'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
]