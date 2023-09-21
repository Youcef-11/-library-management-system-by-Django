from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
 
@login_required(login_url='login')
def index(request):
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Access the username of the currently authenticated user
        username = request.user.username
        username = username[0].upper() + username[1:].lower()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
    


    context = {
        'categories': Category.objects.all(), # 'categories' is the key and 'Category.objects.all()' is the value
        'books': Book.objects.all(),
        'form': BookForm(),
        'category_form': CategoryForm(),
        'all_books': Book.objects.filter(active=True).count(),
        'soldbooks': Book.objects.filter(status='sold').count(),
        'rentedbooks': Book.objects.filter(status='rented').count(),
        'availablebooks': Book.objects.filter(status='available').count(),
        'username': username,
    }
    return render(request, 'pages/index.html', context)

@login_required(login_url='login')
def books(request):
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Access the username of the currently authenticated user
        username = request.user.username
        username = username[0].upper() + username[1:].lower()
    
    title = None
    books = Book.objects.all()
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            books = books.filter(title__icontains=title, active=True)
    
    
    
    
    

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()



    context = {
        'categories': Category.objects.all(), 
        'books': books,
        'category_form': CategoryForm(),
        'username': username,
    }
    return render(request, 'pages/books.html', context)

@login_required(login_url='login')
def update(request, id):


    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Access the username of the currently authenticated user
        username = request.user.username
        username = username[0].upper() + username[1:].lower()
        
    book_id = Book.objects.get(id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book_id)
        if form.is_valid():
            form.save() 
            return redirect('/')
        
    else : 
        form = BookForm(instance=book_id)

    
    context = {
        'form': form,
        'book_id': book_id,
        'username': username,
    }


    return render(request, 'pages/update.html', context)

@login_required(login_url='login')
def delete(request, id):
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Access the username of the currently authenticated user
        username = request.user.username
        username = username[0].upper() + username[1:].lower()
        
    book_to_delete = get_list_or_404(Book, id=id)
    if request.method == 'POST':
        book_to_delete[0].delete()
        return redirect('/')

    context = {'username': username,}
    
    return render(request, 'pages/delete.html', context)