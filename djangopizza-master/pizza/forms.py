from django import forms
from . models import pizza_type
from  django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User

class pizza_data(forms.ModelForm):
    class Meta:
        model =  pizza_type
        fields  = ['pizza','size','topping','price']
        widgets = {
            'pizza': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'topping': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }





class signup(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control my-2'}),
            'first_name':forms.TextInput(attrs={'class':'form-control my-2'}),
            'last_name':forms.TextInput(attrs={'class':'form-control my-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control my-2'}),
        }