from django.contrib import admin
from .models import Book, UserAccount

admin.site.register(Book)
admin.site.register(UserAccount)