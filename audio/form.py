from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Song


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = (
            'username','first_name', 'last_name', 'email', 'password1', 'password2', 
        )


class AddMusic(ModelForm):

    class Meta:
        model = Song
        fields = ('title', 'artist', 'image', 'download', 'description', 'genre', 'country', 'year_release', 'date_upload')
        # labels = {
        #     'title': '',
        #     'description': '',
        #     'image_url': ,
        #     'category': '',
        #     'status': '',
        #     'trailer': '',
        #     'download': '',
        #     'year': '',
        #     'views': '',
        # }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Music Title'}),
            'artist': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Artist'}),
            'download': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Download_link'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
            'genre': forms.Select(attrs={'class':'form-control', 'placeholder':'Genre'}),
            'country': forms.Select(attrs={'class':'form-control', 'placeholder':'Country'}),
            'year': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'year'}),
            'uploaded': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Date Uploaded'}),
        }