from django.shortcuts import render, redirect
from .models import *

def book(request):
    context = {
        "all_books" : Book.objects.all()
    }
    return render(request, 'bAndA/book.html', context)
def author(request):
    context = {
        "all_authors" : Author.objects.all()
    }
    return render(request, 'bAndA/author.html', context)
def book_information(request, id):
    context = {
        "book_info" : Book.objects.get(id=id),
        "all_authors" : Author.objects.all()
    }
    return render(request, 'bAndA/book_display.html', context)
def author_information(request, id):
    context = {
        "author_info" : Author.objects.get(id=id),
        "all_books" : Book.objects.all()
    }
    return render(request, 'bAndA/author_display.html', context)
def book_process(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST["title"], desc=request.POST["desc"])
    return redirect('/book')
def author_process(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], notes=request.POST["notes"])
    return redirect('/author')
def book_add(request, book_id, author_id):
    if request.method == "POST":
        this_book = Book.objects.get(id=book_id)
        this_author = Author.objects.get(id=author_id)
    return redirect('/authors/', author_id)
