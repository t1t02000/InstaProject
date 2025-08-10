from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.home, name='home'),

    # Tu login principal
    path('login/', auth_views.LoginView.as_view(template_name='feed/login.html'), name='login'),

    # Sobrescribe la ruta /accounts/login/ para que NO busque registration/login.html
    path('accounts/login/', auth_views.LoginView.as_view(template_name='feed/login.html'), name='accounts_login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('explore/', views.explore, name='explore'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('register/', views.register, name='register'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow_toggle/<str:username>/', views.follow_toggle, name='follow_toggle'),

    # Mantén esto para reset/change password, etc.
    path('accounts/', include('django.contrib.auth.urls')),
]





