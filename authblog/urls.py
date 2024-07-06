from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.UserLogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('logout/', views.Logout, name='logout'),
    path('passowrd_reset/', auth_views.PasswordResetView.as_view( template_name='authapp/password_reset.html'), name='passowrd_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='authapp/passowrd_reset_complete.html'), name='password_reset_complete'),
    # path('reset_password/', )
]
