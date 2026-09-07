from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title

class UserAccount(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'signup'

    def __str__(self):
        return self.username