from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .models import Comment



# Create your views here.

def index(request):
    return render(request, 'products_store/index.html')

def tools(request):
    return render(request, 'products_store/tools.html')

def contact(request):
    return render(request, 'products_store/contact.html')

def delivery(request):
    return render(request, 'products_store/delivery.html')

def comments_view(request):
    com_consist = {
        'comments': Comment.objects.all()
    }
    return render(request, 'custom_comments/comments_page.html', com_consist)

def reg_form(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration completed {'username'}! Please login.')
            return redirect('products_store-login')
    else:
        form = UserRegisterForm()

    return render(request, 'products_store/register.html', {'form':form})