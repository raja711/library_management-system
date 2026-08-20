"""
URL configuration for rastaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.urls import path
from myapp import views
from django.urls import path, include
from django.contrib import admin



urlpatterns = [

    path('admin/',admin.site.urls),
    path('index/', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('menu/', views.menu),
    path('service/', views.service),
    path('team/', views.team),
    path('testimonial/', views.testimonial),
    path('form/', views.contact),
    path('booking/', views.booking),
    path('order/', views.order),
    path('signup/', views.signup_view, name='signup'),
    path('booking/', views.booking, name='booking'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('library_home', views.library_home, name='library_home'),
    path('add_book/', views.add_book, name='add_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('update_book/', views.update_book, name='update_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),

]

