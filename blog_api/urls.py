from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    path('articles/<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('articles/', PostList.as_view(), name="listcreate")
]