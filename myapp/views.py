from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book

def library_home(request):
    return render(request, 'librabry_home.html')

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        Book.objects.create(title=title, author=author, description=description)
        messages.success(request, "Book successfully add ho gayi hai!")
        return redirect('add_book')

    return render(request, 'add_book.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def update_book(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        try:
            book = Book.objects.get(id=book_id)
            book.title = title
            book.author = author
            book.description = description
            book.save()
            messages.success(request, f"Book ID {book_id} updated successfully!")
        except Book.DoesNotExist:
            messages.error(request, f"Book with ID {book_id} does not exist!")

        return redirect('update_book')

    return render(request, 'update_book.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import UserAccount


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if UserAccount.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'signup.html')

        UserAccount.objects.create(username=username, password=make_password(password))
        messages.success(request, 'Account created successfully!')
        return redirect('signup')

    return render(request, 'signup.html')