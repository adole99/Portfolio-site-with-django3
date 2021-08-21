from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Leave a message...'}), required=True)

    class Meta:
        model = Contact
        fields = '__all__'