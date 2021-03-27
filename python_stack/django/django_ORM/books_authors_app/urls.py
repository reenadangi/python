from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="books" ),
    path('add_book/', views.add_book,name="add_book" ),
    path('authors/', views.authors,name="authors" ),
    path('add_author/', views.add_author,name="add_author" ),
    # path('addnew/', views.addnew,name="userapp_adduser" ),
    path('view_bookDetails/<book_id>/', views.view_bookDetails,name="view_bookDetails" ),
    path('view_authorDetails/<author_id>/', views.view_authorDetails,name="view_authorDetails" ),
    path('add_author_to_book/<book_id>/', views.add_author_to_book,name="add_author_to_book" ),
    path('add_book_to_author/<author_id>/', views.add_book_to_author,name="add_book_to_author" ),
    # path('update/', views.update,name="userapp_update" ),
    
]