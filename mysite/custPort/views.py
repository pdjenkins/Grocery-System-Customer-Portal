from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.template import loader
from .models import Account, CustomerAccount
# Create your views here.
def home(request):

    #dummy return
    return HttpResponse("Hello! This is the home page.")
    
    #use this when the home.html page is written
    #return render(request, 'custPort/home.html', context)

def account(request, account_id):
    #accountinfo = "Account id:" + str(account_id)
    account = get_object_or_404(Account, pk=account_id)
    
    return HttpResponse("This page displays your account info.\n" + account.__str__())
    #return HttpResponse("This page displays your account info.\n" + accountinfo)
    #use when account.html is written
    #return render(request, 'custPort/account.html', {'account':account})