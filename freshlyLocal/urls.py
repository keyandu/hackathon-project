
from django.urls import path, include
from . import views
import debug_toolbar

#<<<<<<< HEAD
#URl config
app_name = 'freshlyLocal'
# urlpatterns = [
#     path('hello/', views.say_hello),
#     path('', views.store, name="store"),
#     path('cart/', views.cart, name="cart"),
#     path('checkout/', views.checkout, name="checkout"),
#
# ]
#=======
## URl config
urlpatterns = [
   path('hello/', views.say_hello),
   path('__debug__/', include('debug_toolbar.urls')),
   path('', views.store, name="store"),
   path('cart/', views.cart, name="cart"),
   path('checkout/', views.checkout, name="checkout"),
]
#>>>>>>> e7f4ef01f931343f7a13f0cbbf9d5a3af6236423
