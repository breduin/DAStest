from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ajax_select import urls as ajax_select_urls
from dasapp.views import BookCreateView

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajax_select/', include(ajax_select_urls)),
    path('create-book/', BookCreateView.as_view(), name='book_create'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)