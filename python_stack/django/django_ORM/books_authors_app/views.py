from django.shortcuts import render,redirect
import json



# Books & Authors

from .models import Books,Authors

# Create your views here.
def home(request):
    context={'books':Books.objects.all()}
    # context={'users':Users.objects.all()}
    
    print(context)
    return render(request,"books_authors_app/home.html",context)
def add_book(request):
    new_book=Books.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    print(new_book)
    return redirect("/")
def add_author(request):
    new_author=Authors.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    print(new_author)
    return redirect("/authors")

def authors(request):
    context={'authors':Authors.objects.all()}
    return render(request,"books_authors_app/authors.html",context)

def view_bookDetails(request,book_id):
    context={'book':Books.objects.get(id=book_id),'authors':Books.objects.get(id=book_id).authors.all(),'all_authors':Authors.objects.exclude(books=Books.objects.get(id=book_id))}
   
    print(context)
    return render(request,"books_authors_app/view_bookDetails.html",context)

def view_authorDetails(request,author_id):
    context={'author':Authors.objects.get(id=author_id),'books':Authors.objects.get(id=author_id).books.all(),'all_books':Books.objects.exclude(authors=Authors.objects.get(id=author_id))}
    print(context)
    return render(request,"books_authors_app/view_authorDetails.html",context)

def add_author_to_book(request,book_id):
    bk=Books.objects.get(id=book_id)
    bk.authors.add(Authors.objects.get(id=request.POST['author']))
    print(f"****************added this Author {request.POST['author']} to {book_id}****")
    return redirect(f"/view_bookDetails/{book_id}")

def add_book_to_author(request,author_id):
    au=Authors.objects.get(id=author_id)
    print(request.POST['book'])
    au.books.add(Books.objects.get(id=request.POST['book']))
    print(f"****************added this Book{request.POST['book']} to {author_id}****")
    return redirect(f"/view_authorDetails/{author_id}")
