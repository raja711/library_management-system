# from django.http import HttpResponse
# from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect







# Create your views here.

def index(request):
    return render(request,"index.html" )

def about(request):
    return render(request,"about.html")

def booking(request):
    return render(request,"booking.html")

def contact(request):
    return render(request,"contact.html")

def menu(request):
    return render(request,"menu.html")

def service(request):
    return render(request,"service.html")

def team(request):
    return render(request,"team.html")

def testimonial(request):
    return render(request,"testimonial.html")

def table(request):
    return render(request,"table.html")

def order(request):
    return render(request,"order.html")

def signup(request):
    return render(request,"signup.html")

from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, 'contact.html', {'msg': 'send massage'})
    messages.success(request, "Data successfully saved !")

    return render(request, 'contact.html')




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking

def booking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        table = request.POST.get('table')
        message = request.POST.get('message')


        Booking.objects.create(
            name=name,
            email=email,
            date=date,
            table=table,
            message=message
        )

        messages.success(request, "Aapki table booking successfully ho gayi hai!")
        return redirect('booking')

    return render(request, 'booking.html')



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


        hashed_password = make_password(password)
        UserAccount.objects.create(username=username, password=hashed_password)

        messages.success(request, 'Account created successfully!')
        return redirect('signup')

    return render(request, 'signup.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile  # Model import zaroor karein

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')

        # Username validation
        if UserProfile.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # Email validation
        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        # Database me save karein
        user = UserProfile(
            username=username,
            password=password,
            email=email,
            full_name=full_name
        )
        user.save()

        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')


from django.shortcuts import render, redirect

# Home Page View
def library_home(request):
    return render(request, 'library_home.html')

# Placeholder views for navigation links
def add_book(request):
    return render(request, 'add_book.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def update_book(request):
    return render(request, 'update_book.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book  # <--- Yeh line add karein

def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        # Ab 'Book' model sahi se kaam karega
        Book.objects.create(
            title=title,
            author=author,
            description=description
        )
        messages.success(request, "Book successfully add ho gayi hai!")
        return redirect('add_book')
        return redirect('add_book')

    return render(request, 'add_book.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book


def update_book(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')

        try:
            # Book ID ke hisab se record khojein
            book = Book.objects.get(id=book_id)

            # Record update karein
            book.title = title
            book.author = author
            book.description = description
            book.save()

            messages.success(request, f"Book ID {book_id} updated successfully!")
        except Book.DoesNotExist:
            messages.error(request, f"Book with ID {book_id} does not exist!")

        return redirect('update_book')

    return render(request, 'update_book.html')


from django.shortcuts import render
from .models import Book

def book_list(request):
    # Database se saari books fetch karke template me pass karna
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, book_id):
    # Book ID ke basis par specific book fetch karna
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Login

def login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')

        if u_name and p_word:
            # SQL table 'login' mein record insert karega
            Login.objects.create(username=u_name, password=p_word)
            messages.success(request, "Data successfully saved in database!")
            return redirect('login')
        else:
            messages.error(request, "Please fill out all fields!")

    return render(request, 'login.html')