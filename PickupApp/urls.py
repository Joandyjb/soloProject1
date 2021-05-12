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
    path('UserPost', views.create_post),
    path('like_post/<int:post_id>', views.like_post),
    path('Usercomment/<int:post_id>', views.create_comment),
    path('like_comment/<int:comment_id>', views.like_comment),
    path('user/logout', views.logout),
    path('profile/<int:the_userInfo_id>', views.edit),
    path('ProfileUpdate/<int:the_userInfo_id>', views.Update),
    path('AllCourt', views.Allcourt),
    path('court/<int:courtid>', views.court),
    path("courtcount/<int:courtid>", views.countup),
    path('courtdown/<int:courtid>', views.nocount)


]