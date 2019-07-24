from django.urls import path
from . import views as v

app_name = 'groups'

urlpatterns = [
    path('groups_list/',v.List_Groups.as_view(),name='groups_list'),
    path('new_group/',v.Create_Group.as_view(),name='create_group'),
    path('posts/in/<slug>/',v.Single_Group.as_view(),name='single'),
    path('join/<slug>/',v.Join_Group.as_view(),name='join'),
    path('leave/<slug>/',v.Leave_Group.as_view(),name='leave'),
]