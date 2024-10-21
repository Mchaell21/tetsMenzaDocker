from django import forms
from .models import ImageServ, LogoImg

class ImageForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukan Judul Gambar'}))
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Berikan sedikit deskripsi tentang gambar'}))

    class Meta:
        model = ImageServ
        fields = ['title', 'description', 'image', 'is_enabled']

class LogoForm(forms.ModelForm):
    titleLogo = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukan Nama Logo'}))
    
    class Meta:
        model = LogoImg
        fields = ['titleLogo', 'image', 'is_enabled']
