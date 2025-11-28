from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateDetailsForm, User_profileUpdateForm
from django.contrib import messages
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .forms import CommentForm


# Create your views here.

def index(request):
    return render(request, 'products_store/index.html')

def tools(request):
    comments = {
        'comments': Comment.objects.all(),
    }
    return render(request, 'products_store/tools.html', comments)

def contact(request):
    return render(request, 'products_store/contact.html')

def delivery(request):
    return render(request, 'products_store/delivery.html')

def comments_view(request):
    com_consist = {
        'comments': Comment.objects.all(),
    }
    return render(request, 'products_store/comments_page.html', com_consist)

class CommentsList(ListView):
    model = Comment
    template_name = 'products_store/tools.html'
    com_consist_object_name = 'comments'
    com_sorting = ['-commented_date']

class CommentsDetail(DetailView):
    model = Comment

class CommentsCreate(CreateView):
    model = Comment
    fields = ['comname', 'comtext']
    # form_class = CommentForm
    # template_name = 'products_store/comment_form.html'

    def comment_form(self, form):
        form.instance.comwriter = self.request.user
        return super().comment_form(form)
    
class CommentsUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comname', 'comtext']

    def comment_form(self, form):
        form.instance.comwriter = self.request.user
        return super().comment_form(form)
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.comwriter:
            return True
        return False
    
class CommentsDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = "products_store-tools"

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.comwriter:
            return True
        return False

def reg_form(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration completed {username}! Please login.')
            return redirect('products_store-login')
    else:
        form = UserRegisterForm()

    return render(request, 'products_store/register.html', {'form':form})

@login_required
def basket_page(request):
    return render(request, 'products_store/basket.html')

@login_required
def profile_page(request):
    if request.method == 'POST':
        uud_form = UserUpdateDetailsForm(request.POST, instance=request.user)
        upu_form = User_profileUpdateForm(request.POST, request.FILES, instance=request.user.user_profile)

        if uud_form.is_valid() and upu_form.is_valid():
            uud_form.save()
            upu_form.save()
            messages.success(request, f'User details successfuly updated!')
            return redirect('products_store-profile_page')
    else:
        uud_form = UserUpdateDetailsForm(instance=request.user)
        upu_form = User_profileUpdateForm(instance=request.user.user_profile)



    content = {
        'uud_form': uud_form,
        'upu_form': upu_form
    }
    return render(request, 'products_store/profile.html', content)