from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:id>/', views.blog_details, name='blog_details'),
    path('create/', views.create_blog, name='create_blog'),
    path('blog/<int:id>/update/', views.update_blog, name='update_blog'),
    path('blog/<int:id>/delete/', views.delete_blog, name='delete_blog'),
    path('login/', views.UserLogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('passowrd_reset/', auth_views.PasswordResetView.as_view( template_name='authblog/password_reset.html'), name='passowrd_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authblog/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='authblog/passowrd_reset_complete.html'), name='password_reset_complete'),
    # path('reset_password/', )
]
