from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_profile/', views.user_change, name='change_profile'),
    path('password/', views.pass_change, name='pass_change'),
    path('add_picture/', views.add_profile_picture, name='add_picture'),
    path('change_profile_picture/', views.change_pro_pic, name='change_profile_picture'),
]
