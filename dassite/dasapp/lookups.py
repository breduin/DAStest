from ajax_select import register, LookupChannel
from .models import *

@register('authors')
class AuthorsLookup(LookupChannel):

    model = Author
    min_length = 1 # Minimum number of characters user types before a search is initiated.

# Queryset matching the characters typed by the user
    def get_query(self, q, request):
        qs = self.model.objects.filter(name__startswith=q)[:10]
        return qs

    def format_item_display(self, item):
        return u"<span class='tag'> %s</span>" % (item.name)

    def format_match(self, obj):
        return u"<span class='tag'> %s,  author </span>" % (obj.name)
