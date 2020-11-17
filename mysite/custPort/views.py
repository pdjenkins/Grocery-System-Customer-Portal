from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import forms
from .models import Account, CustomerAccount
#from .forms import createAccountForm
# Create your views here.
def home(request):

    #dummy return
    #return HttpResponse("Hello! This is the home page.")
    
    #use this when the home.html page is written
    return render(request, 'custPort/home.html')

def account(request, username):
    try:
        account = Account.objects.get(username_text=username)
    except Account.DoesNotExist:
        account = None
        return HttpResponse("This account could not be found.")
    return render(request, 'custPort/account.html', {'account':account})

class CreateAccount(CreateView):
    model = Account
    fields = ['username_text', 'password_text', 'name_text', 'account_number']
    success_url="/custPort/"
class CreateCustomerAccount(CreateView):
    model = CustomerAccount
    fields = ['username_text', 'password_text', 'name_text', 'account_number', 'address_text', 'bill_address_text', 'email_text', 'CC_info', 'save_CC']
    success_url="/custPort/"

def sign_in_form (request):
    form = forms.SignIn()
    if request.method == 'POST':
        form = forms.SignIn(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            #if this works then this view should have the information
            #now we can check if the user exists
            return redirect('custPort:account', username=user_name)
    else:
        form = forms.SignIn(request.GET)
    return render(request, 'custPort/sign_in.html',{'form': form })