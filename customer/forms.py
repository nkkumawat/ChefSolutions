from django import forms

class loginForm(forms.Form):
    email = forms.EmailField(label="email", max_length=100)
    password = forms.CharField(label="password", max_length=100)


class signUpForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    email = forms.EmailField(label="email", max_length=100)
    mobile = forms.CharField(label="mobile", max_length=10)
    password = forms.CharField(label="password", max_length=100)