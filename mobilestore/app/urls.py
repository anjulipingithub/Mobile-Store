
from django.urls import path
from .views import *
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path("",views.Home,name="ah"),
    path("category/<slug:value>",CategoryView.as_view(),name="category"),
    path('addcart/<int:pid>/',addcart,name='addcart'),
    path('MyCart/',MyCart.as_view(),name="mycart"),
   
    path('delcart/<int:pid>',delcart,name='delcart'),
    path('buy/<int:pid>', BuyView.as_view(), name='buy'),
    path('ordersuccess/', OrderSuccessView.as_view(), name='ordersuccess'),
    path('review/<int:pid>/',addreview, name='addr'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

