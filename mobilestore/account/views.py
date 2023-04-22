from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import RegForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models  import CustUser
# Create your views here.
class Home(TemplateView):
    template_name="home.html"

class Reg(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=CustUser
    success_url=reverse_lazy("h")

class Log(FormView):
  template_name="log.html"
  form_class=LoginForm    
  
  def post(self,request,*args,**kwargs):
   form_data=LoginForm(data=request.POST)
   if form_data.is_valid():
     un=form_data.cleaned_data.get("username")
     pw=form_data.cleaned_data.get("password")
     user=authenticate(request,username=un,password=pw)
     if user: 
      login(request,user)
      messages.success(request,"login successfull")
      return redirect("ah")
     else:
      messages.error(request,"login failed!! username or password  incorrect")
      return render(request,"reg.html",{"form":form_data})   
   else:
    messages.error(request,"login failed!!")
    return render(request,"log.html",{"form":form_data})  
   




   
