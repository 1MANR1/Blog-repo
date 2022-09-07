"""Defines URL patterns for blogs"""
from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
	# Home page 
	path('', views.blogs, name='blogs'),
	# Page for adding new blog
	path('new_blog/', views.new_blog, name='new_blog'),
	# Page for editing URLs
	path('edit_blog/<int:blog_id>', views.edit_blog, name='edit_blog'),
]