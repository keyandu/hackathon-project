from django.db import models
import datetime
from django.contrib.auth.models import User 
# Create your models here.



#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    home_address = = models.ManyToManyField(
#         'Address', 
#         through='AddressInfo'
#         through_fields=('address', 'profile')
#    )

#class AddressInfo(models.Model):
#    HOME_ADDRESS = 1
#    SHIPPING_ADDRESS = 2

#    TYPE_ADDRESS_CHOICES = (
#        (HOME_ADDRESS, "Home address"),
#        (SHIPPIN_ADDRESS, "Shipping address"),
#    )

#    address = models.ForeignKey('Address', on_delete=models.CASCADE)
#    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

#    # This is the field you would use for know the type of address.
#    address_type = models.PositiveIntegerField(choices=TYPE_ADDRESS_CHOICES)
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def get_all_categories():
        return Categroy.objects.all()
    def __str__(self):
        return self.category_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=100,null=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nickname

    def register(self):
        self.save()
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    

class Products(models.Model):
    produce_name = models.CharField(max_length=100,null=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Products.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()



class Orders(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_ordered = models.DateField(default=datetime.datetime.today)
    complete = models.BooleanField(default=False,null=True,blank = False)
    transaction_id = models.CharField(max_length=200, null=True)
class OrderItem(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_ordered = models.DateField(default=datetime.datetime.today)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_ordered = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.address