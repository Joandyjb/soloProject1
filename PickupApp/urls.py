from django.urls import path
from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'map', views.default_map, name="default"),
    path('', views.index),
    path('user/create', views.create),
    path('user/login', views.login),
    path('login', views.userlog),
    path('user/success', views.success),
    path('user/logout', views.logout),
    path('profile/<int:the_userInfo_id>', views.edit),
    path('ProfileUpdate/<int:the_userInfo_id>', views.Update),
    path('AllCourt', views.Allcourt),
    path('court/<int:courtid>', views.court),
    path("courtcount/<int:courtid>", views.countup),
    path('courtdown/<int:courtid>', views.nocount)


]