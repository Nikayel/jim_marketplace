from django.contrib import admin
from django.urls import path, include
from main_app.views import index, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('main_app.urls')),
    path('items/', include('item.urls')),
    path('listing/', include('listing.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
