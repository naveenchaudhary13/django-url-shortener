from django import forms
from shortener.models import ShortURL


class ShortURLForm(forms.ModelForm):
    """Form for shortening a long URL."""
    class Meta:
        model = ShortURL
        fields = ['long_url']
        labels = {
            'long_url': '',
        }
        widgets = {
            'long_url': forms.URLInput(attrs={
                'placeholder': 'Enter your long URL here...',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500',
                'required': True,
            })
        }
