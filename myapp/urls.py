from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_home, name='library_home'),
    path('add_book/', views.add_book, name='add_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('update_book/', views.update_book, name='update_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('signup/', views.signup_view, name='signup'), # Yeh line add karein
]