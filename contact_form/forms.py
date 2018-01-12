from django import forms
from .models import UserData


class ContactForm(forms.ModelForm):

    class Meta:
        model=UserData
        fields=[
            "name",
            "surname",
            "choice",
            "email",
            "message",
        ]

