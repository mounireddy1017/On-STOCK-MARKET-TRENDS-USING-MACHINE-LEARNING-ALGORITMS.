from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class stock_market_model(models.Model):


    Company_Name= models.CharField(max_length=300)
    Company_Category= models.CharField(max_length=300)
    Opening_Price= models.CharField(max_length=300)
    Date_Of_Opening= models.CharField(max_length=300)
    Closing_Price= models.CharField(max_length=300)
    Date_Of_Closing= models.CharField(max_length=300)
    volume= models.CharField(max_length=300)
    Profit= models.CharField(max_length=300)
    prices_drop= models.CharField(max_length=300)
    Stock_Market_Trends= models.CharField(max_length=300)
    Stock_Exchange_By= models.CharField(max_length=300)


class predicting_stock_markettrends_model(models.Model):

    names= models.CharField(max_length=300)
    Company_Category= models.CharField(max_length=300)
    Opening_Price= models.CharField(max_length=300)
    Date_Of_Opening= models.CharField(max_length=300)
    Closing_Price= models.CharField(max_length=300)
    Date_Of_Closing= models.CharField(max_length=300)
    volume= models.CharField(max_length=300)
    Profit= models.CharField(max_length=300)
    prices_drop= models.CharField(max_length=300)
    Stock_Market_Trends= models.CharField(max_length=300)
    Stock_Exchange_By= models.CharField(max_length=300)


class search_ratio_model(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



