from django.db import models

# Create your models here.

#A parent class that carries the basic info of all user accounts in the system
class Account(models.Model):
    #Each variable has to adhere to the Field class.
    #For example, name_text is a CharField - basically a string variable for the model
    
    #Each field is a column in the database, and each row of said database is an instance of this class
    username_text = models.CharField(max_length=200)
    password_text = models.CharField(max_length=200)#temporary, super vulnerable and BAD password storage
    name_text = models.CharField(max_length=200)
    account_number = models.IntegerField(-1) #negative to show the account is not complete, this should only change when all other fields are filled.
    #to string of class
    #might want to change this to just name_text, depends on how we use this method...
    def __str__(self):
        return "user: " + self.username_text + ", pass: " + self.password_text + ", name: " + self.name_text + ", account# " + str(self.account_number)
    
class CustomerAccount(models.Model):
    #this links the 'Customer' account to the 'Account' parent class
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    #account data
    address_text = models.CharField(max_length=200)
    bill_address_text = models.CharField(max_length=200)
    email_text = models.CharField(max_length=200)
    CC_info = models.CharField(max_length=200)
    save_CC = models.BooleanField(False)
    #to string of class
    #might want to change this to just the account.name_text, depends on how we use this method...
    def __str__(self):
        return self.address_text + ", " + self.bill_address_text + ", " + self.email_text + ", " + self.CC_info + ", save_CC=" + str(self.save_CC)