from django.urls import path
from . import views
from .views import AccountCreate
app_name = 'custPort'
#all paths will have an associated example comment of what the URL would have for it to work
urlpatterns = [
    #example: /custPort/
    path('', views.home, name='home'),
    #example: /custPort/1/
    path('<int:account_id>/', views.account, name='account'),
    path('createaccount/', AccountCreate.as_view(), name='createaccount')
]