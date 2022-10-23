from django.urls import path
from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('grid/<int:pk>/', Pagelistinggrid.as_view(), name='grid'),
    path('detail_product/<int:pk>/', Pagedetailproduct.as_view(), name='detail_product'),
    path('bolimlar/<str:nom>/', BolimView.as_view(), name='bolimlar'),
]