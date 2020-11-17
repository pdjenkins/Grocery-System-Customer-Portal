from django.urls import path
from . import views
from .views import CreateAccount, CreateCustomerAccount
app_name = 'custPort'
#all paths will have an associated example comment of what the URL would have for it to work
urlpatterns = [
    #example: /custPort/
    path('', views.home, name='home'),
    #example: /custPort/1/
    path('account/<username>/', views.account, name='account'),
    path('createaccount/', CreateAccount.as_view(), name='createaccount'),
    path('createcustomeraccount/', CreateCustomerAccount.as_view(), name='create_customer_account'),
    path('signin/', views.sign_in_form, name='sign_in_form'),
]