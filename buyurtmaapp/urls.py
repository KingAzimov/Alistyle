from django.urls import path
from .views import *

urlpatterns = [
    path('tanlangan/', TanlanganView.as_view(), name='wishlist'),
    path('savat/', SavatView.as_view(), name='cart'),
    path('buyurtma/', BuyurtmaView.as_view(), name='orders'),
]