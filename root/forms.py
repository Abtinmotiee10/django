from django import forms

class NewsLetterform(forms.Form):
    email = forms.EmailField()