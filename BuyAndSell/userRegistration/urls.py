from django.urls import path
from django.contrib.auth import views as auth_views


from . import views 
from userRegistration.views import index,register,userInfoFrom,NewBookForm

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='registerform'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name="loginform"),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('userinfo/',views.userInfoFrom,name="userinfoform"),
    path('newbook/',views.NewBookForm,name="newbookform")
]
