from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mein.views import *

urlpatterns = [

    path('',Index_View.as_view(),name='index'),
    path('category/',Category_View.as_view(),name='category'),
    path('contact/',Contact_View.as_view(),name='contact'),
    path('single/',Single_View.as_view(),name='single'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)