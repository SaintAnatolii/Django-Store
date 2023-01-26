# ! базовые формы для авторизации и регистрации
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password']
        
class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя',
        'id': 'inputFirstName'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию',
        'id': 'inputLastName'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя',
        'id': 'inputUsername'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты',
        'id': 'inputEmailAddress'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль',
        'id': 'inputPassword'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Подтвердите пароль',
        'id': 'inputConfirmPassword'}))
    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'email', 'password1', 'password1']

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputFirstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputLastName'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputUsername',
        'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'id': 'inputEmailAddress',
        'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
        'id': 'userAvatar'}), required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'username', 'email']
