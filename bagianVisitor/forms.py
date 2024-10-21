from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Contact
import json
from django.forms.widgets import DateInput
from captcha.fields import CaptchaField

class contactForm(forms.ModelForm):
    contactName = forms.CharField(label='Nama', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Nama'}))
    contactEmail = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Email'}))
    contactPhone = forms.CharField(label='Telepon', widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Telepon'}))
    contactNote = forms.CharField(label='Catatan', widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Masukkan Catatan'}))
    captcha = CaptchaField(label='')

    class Meta:
        model = Contact
        fields = ['contactName','contactEmail','contactPhone','contactNote','captcha']
