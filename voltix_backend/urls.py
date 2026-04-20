from django.contrib import admin
from django.urls import path, include # Make sure 'include' is here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')), # This tells Django to look in your store app for the home page
]

# Add this at the end to allow image viewing during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)