from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): #UserCreationForm 클래스를 상속하여 만들었다.
    email = forms.EmailField(label="이메일") #이메일 형식으로 제대로 입력했는지 확인

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")