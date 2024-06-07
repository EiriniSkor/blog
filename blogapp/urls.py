
from blogapp import views
from django.urls import path
from django.contrib import admin

app_name='blogapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('blogs/', views.blogs, name='blogs'),
    path('about/', views.about, name='about'),
]