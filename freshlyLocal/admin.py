from django.contrib import admin
from freshlyLocal.models import Category,Customer,Products,Orders,OrderItem,ShippingAddress
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass;
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

