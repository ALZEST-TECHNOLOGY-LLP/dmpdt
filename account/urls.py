
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    # path('signup/', views.user_signup, name='user_signup'),
    path('logout/', views.logout_v, name='logout_v'),
    path('changepassword/', views.change_password, name='change_password'),
    path('resetpassword/', views.reset_password, name='reset_password'),
    path('chbyempassword/<token>/', views.chbyempassword, name='chbyempassword'),
    path('pass_reset_done/', views.pass_reset_done, name='pass_reset_done'),

]