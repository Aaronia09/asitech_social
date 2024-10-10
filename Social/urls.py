   # Social/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import notifications, register, user_login, create_post, post_detail, add_comment, like_post, profile_view, home

urlpatterns = [
    path('home/', home, name='home'), 
     path('', register, name='register'),
       path('login/', user_login, name='login'),
       path('logout/', auth_views.LogoutView.as_view(), name='logout'),
       path('post/create/', create_post, name='create_post'),
       path('post/<int:post_id>/', post_detail, name='post_detail'),
       path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
       path('post/<int:post_id>/like/', like_post, name='like_post'),  
       path('profile/', profile_view, name='profile'),
       path('notifications/', notifications, name='notifications'), 
   ]