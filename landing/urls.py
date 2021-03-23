from django.urls import path
from landing.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)