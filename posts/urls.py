from  django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name="create_post"),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/delete/', views.delete_account, name='delete_account'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
