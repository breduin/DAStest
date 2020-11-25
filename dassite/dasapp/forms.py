from django import forms
from .models import Book
from ajax_select.fields import AutoCompleteSelectField

class BookCreateForm(forms.ModelForm):
    author = AutoCompleteSelectField('authors', required=True, help_text='Start typing with J', label='Author')

    class Meta:
        model = Book
        fields = '__all__'