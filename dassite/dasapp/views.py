from .models import Book
from .forms import BookCreateForm
from . import models
from django.views.generic import CreateView
from ajax_select.fields import autoselect_fields_check_can_add


class BookCreateView(CreateView):
    model = Book
    template_name = 'book_form.html'
    success_url = '/admin/'

    def get_form_class(self):
        autoselect_fields_check_can_add(BookCreateForm, self.model, self.request.user)
        return BookCreateForm

