# this page is where my blog urls live. this takes what the url is called and links it with the
# correct view

from django.urls import path
from .views import BlogView, PostTemplateView, AddPostView, UpdatePostView, DeletePostView, AllPostsView

urlpatterns = [
    
    path('', BlogView.as_view(), name='blogpage'),
    path('article/<int:pk>', PostTemplateView.as_view(), name='post-details'),
    path('add', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('allposts', AllPostsView.as_view(), name='all-posts'),

]