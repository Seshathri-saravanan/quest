from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('historical',views.historical,name='historical'),
    path('temples',views.temples,name='temples'),
    path('parks',views.parks,name='parks'),
    path('cities',views.cities,name='cities'),
    path('beaches',views.beaches,name='beaches'),
    path('hills',views.hills,name='hills'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('blog',views.blog,name='blog'),

]