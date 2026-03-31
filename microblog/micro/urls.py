from os import name

from django.urls import path
from .import views

urlpatterns = [
   path('', views.home, name='home'),
   path('new_blog/', views.new_blog, name='new_blog'),
   path('update_blog/<int:id>', views.update_blog, name='update_blog'),
   path('delete_blog/<int:id>', views.delete_blog, name='delete_blog')
]

