from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User_profile
from .models import Comment

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateDetailsForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class User_profileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User_profile
        fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comname', 'comtext']
        labels = {
            "comname": "Name", "comtext": "Comment",
        }
        widgets = {
            "comtext": forms.Textarea(attrs={"rows": 3})
        }