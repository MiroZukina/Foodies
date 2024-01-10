from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='blog-home'),  
    path('profile_list/',views.profile_list, name='profile_list'),
    path('profile/<int:pk>',views.profile, name='profile'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('update_user/',views.update_user, name='update_user'),
    path('post_like/<int:pk>',views.post_like, name='post_like'),
    path('post_show/<int:pk>',views.post_show, name='post_show'),
    path('unfollow/<int:pk>',views.unfollow, name='unfollow'),
    path('follow/<int:pk>',views.follow, name='follow'),
    path('delete_post/<int:pk>',views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>',views.edit_post, name='edit_post'),
    path('search/',views.search, name='search'),
    path('search_user/',views.search_user, name='search_user'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='blog/password_reset.html'
         ), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'
         ), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='blog/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='blog/password_reset_complete.html'
         ),
         name='password_reset_complete')
    
      
]