# school_library/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.library_home, name='library_home'),
    path('users/', views.user_list, name='user_list'),
    # path('user/<int:user_id>/', views.user_update, name='user-update'),
    path('user/new/', views.add_user, name='add_user'),
    path('check-email/', views.check_email, name='check_email'),
#     path('borrow/', views.borrow_book, name='borrow_book'),
#     path('return/<int:borrow_id>/', views.return_book, name='return_book'),
#     path('borrow-list/', views.borrow_list, name='borrow_list'),
#     path('search/', views.search_books, name='search_books'),
#     path('fetch-book-data/', views.fetch_book_data, name='fetch_book_data'),
]

