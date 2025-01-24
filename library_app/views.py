# library_app/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm


def library_home(request):
    return render(request, 'library_app/index.jinja')

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            return render(request, 'library_app/user_form.jinja', {'form': form})
    else:
        form = UserForm()
        return render(request, 'library_app/user_form.jinja', {'form': form})




# def update_user(request, user_id):
#     user = get_object_or_404(User, user_id=user_id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('user_list')
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'user_update.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'library_app/view_users.jinja', {'users': users})

def check_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)