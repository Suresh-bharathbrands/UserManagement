from django import forms
from subapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields = ['S_no', 'Notes']
       
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        

class CreateUserForm(forms.ModelForm):
    class Meta:
        model=CreateUser
        fields = ['user_name', 'date_of_birth', 'user_profile', 'status']
       
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'