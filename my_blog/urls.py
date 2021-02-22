
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blogHome, name="blog"),
    path('edit_blogpost/<str:slug>', views.EditBlog, name="edit_blog"),
    path('search/', views.search, name="search"),
    path('blogpost/<str:slug>', views.blogPost, name="blogpost"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('msg_detail/<str:pk>', views.msgDetails, name="msg_detail"),
    path('create_blog/', views.createBlog, name="create_blog"),
    path('dashboard/', views.Dashboard, name="dashboard"),
    path('login_page/', views.Dashboard, name="login_page"),
]
