from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='feed/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Rutas fijas antes de rutas dinámicas para evitar colisiones
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow_toggle/<str:username>/', views.follow_toggle, name='follow_toggle'),
]