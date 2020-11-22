from django.urls import path, re_path

from . import views

urlpatterns = [
    path('tmp',views.tmp,name="tmp"),
    path('verifyemail',views.verifyemail,name="verifyemail"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")

]