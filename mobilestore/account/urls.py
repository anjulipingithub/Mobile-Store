from django.urls import path
from account.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
     path('main/',Home.as_view(),name="mh"),
     path('reg/',Reg.as_view(),name="reg"),
     path('log/',Log.as_view(),name="log"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)