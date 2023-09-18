from django.shortcuts import render, redirect, get_list_or_404
from .models import *
from .forms import *
# Create your views here.



def index(request):

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
    }
    return render(request, 'pages/index.html', context)


def books(request):

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()



    context = {
        'categories': Category.objects.all(), # 'categories' is the key and 'Category.objects.all()' is the value
        'books': Book.objects.all(),
        'category_form': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)


def update(request, id):

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
    }


    return render(request, 'pages/update.html', context)


def delete(request, id):
    book_to_delete = get_list_or_404(Book, id=id)
    if request.method == 'POST':
        book_to_delete[0].delete()
        return redirect('/')
    return render(request, 'pages/delete.html')