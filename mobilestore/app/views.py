from django.shortcuts import render,redirect
from urllib import request
from django.http import HttpResponse
from django.views import View
from .models import *
from django.views.generic import TemplateView,FormView
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
def Home(request):
    return render(request,"app/home2.html")

class CategoryView(View):
    def get(self,request,value):
        product=Product.objects.filter(category=value)
        title=Product.objects.filter(category=value).values('title')
        return render(request,"app/category.html",locals())




class MyCart(TemplateView):
    template_name='cart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Cart.objects.filter()
        return context
    
def addcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    product=Product.objects.get(id=id)
    user=request.user
    Cart.objects.create(product=product,user=user)
    return redirect('ah')
def delcart(request,*args,**kwargs):
    id=kwargs.get("pid")
    user=request.user
    Cart.objects.filter(id=id).delete()
    return redirect('mycart')
def addreview(request, pid):
    if request.method=="POST":
        id = pid
        product = Product.objects.get(id=id)
        user = request.user
        cmnt = request.POST.get("comment")
        Review.objects.create(product=product, user=user, comment=cmnt)
        return redirect('ah')    
class BuyView(TemplateView):
    template_name = 'buy.html'
    def post(self, request, *args, **kwargs):
        user = request.user
        products = Cart.objects.filter(user=user).values_list('mobile', flat=True)
        total_cost = sum(Cart.objects.filter(user=user).values_list('mobile__prize', flat=True))
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Process payment
            buy = Buy.objects.create(user=user, total_cost=total_cost)
            buy.products.set(products)
            Cart.objects.filter(user=user).delete()
            return redirect('ordersuccess')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)  
class PaymentView(FormView):
    template_name = 'payment.html'
    form_class = PaymentForm
    success_url = 'ordersuccess'

    def form_valid(self, form):
        # Process payment
        return super().form_valid(form)        

class OrderSuccessView(TemplateView):
    template_name = 'ordersuccess.html'          
        