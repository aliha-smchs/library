# library_app/views.py
from django.shortcuts import render



def library_home(request):
    return render(request, 'library_app/index.jinja')
