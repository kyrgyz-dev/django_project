from django.urls import path
from user import views

# user/
urlpatterns = [
    path('', views.get_all_users),
    path('<int:user_id>/', views.get_user),
    path('add/', views.add_user),
    path('edit/<int:user_id>/', views.edit_user),
    path('delete/<int:user_id>/', views.delete_user),
]
