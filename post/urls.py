from django.urls import path
from post.views import get_posts, get_post, create_post, edit_post, delete_post

app_name = 'post'

urlpatterns = [
    path('', get_posts, name='post-list'),
    path('create/', create_post, name='post-create'),
    path('<int:pk>/', get_post, name='post-detail'),
    path('<int:pk>/edit/', edit_post, name='post-edit'),
    path('<int:pk>/delete/', delete_post, name='post-delete'),

]
