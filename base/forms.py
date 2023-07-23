from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name', 'surname', 'message', 'email', 'phone']
class ProductApplyForm(forms.ModelForm):
    class Meta:
        model=ProductApply
        fields=['name', 'email', 'phone']
class HomeApplyForm(forms.ModelForm):
    class Meta:
        model=HomeApply
        fields=['email',] 
