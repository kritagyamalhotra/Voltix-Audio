from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your existing paths ...
] 

# Add this at the end to allow image viewing during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)