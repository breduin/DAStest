from django.contrib import admin
from .models import *
from .forms import BookCreateForm
from ajax_select.admin import AjaxSelectAdmin


admin.site.register(Author)

@admin.register(Book)
class BookAdmin(AjaxSelectAdmin, admin.ModelAdmin):
    form = BookCreateForm
    list_display = ('name',
                    'author'
                    )


