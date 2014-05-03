# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    #Django’s form system automatically looks for any method whose name starts with clean_ and ends with the name of a field. 
    #If any such method exists, it’s called during validation.
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 1:
            raise forms.ValidationError("Not enough words!")
        return message