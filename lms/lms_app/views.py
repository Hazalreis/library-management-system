from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect('/')
        
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'category' : Category.objects.all() ,
        'books' : Book.objects.all(),
        'form' : BookForm(),
        'formcat' : CategoryForm(),
        'allbooks' : Book.objects.filter(active=True).count(),
        'booksold' : Book.objects.filter(status='sold').count(),
        'bookavalible' : Book.objects.filter(status='avalible').count(),
        'bookrental' : Book.objects.filter(status='rental').count(), 
    }

    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = Book.objects.filter(title__icontains=title
            ) | Book.objects.filter(author__icontains=title)




    context = {
      'category' : Category.objects.all() ,
      'books' : search,
      'formcat' : CategoryForm(),
    }
    
    return render(request, 'pages/books.html', context)


def update(request, id):
    book_id = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')

    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form': book_save
    }
    return render(request, 'pages/update.html', context)


def delete(request, id):
    book_remove = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_remove.delete()
        return redirect('/')
    return render(request, 'pages/delete.html', {'book': book_remove})