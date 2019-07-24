from django.urls import path
from . import views as v

app_name = 'posts'

urlpatterns = [
    path('posts/',v.Post_List.as_view(),name='post_list'),
    path('new_post/',v.Create_Post.as_view(),name='create_post'),
    path('user_posts/<str:username>/',v.User_Posts.as_view(),name='user_posts'),
    path('post_detail/<username>/<int:pk>/',v.Post_Detail.as_view(),name='post_detail'),
    path('post_delete/<int:pk>/',v.Delete_Post.as_view(),name='delete_post'),
]