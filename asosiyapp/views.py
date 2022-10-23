from django.shortcuts import render
from django.db.models import Count
from django.views import View
from .models import *


class Home2View(View):
    def get(self, request):
        data={
            'bolimlar':Bolim.objects.all()[:6],
            'davomi':Bolim.objects.all()[6:]
        }
        return render(request, 'page-index-2.html', data)

class HomeView(View):
    def get(self, request):
        data={
            'bolimlar':Bolim.objects.all()[:6],
            'davomi':Bolim.objects.all()[6:]
        }
        return render(request, 'page-index.html', data)

class BolimlarView(View):
    def get(self, request):
        context = {
            'bolimlar': Bolim.objects.all()
        }
        return render(request, 'page-category.html', context)

class BolimView(View):
    def get(self, request, pk):
        data={
            'ichkilar':Ichki.objects.filter(bolim__id=pk),
            'bolimlar':Bolim.objects.get(id=pk)
        }
        return render(request, 'ichki.html', data)

class Pagelistinggrid(View):
    def get(self, request, pk):
        data={
            'mahsulotlar':Mahsulot.objects.filter(ichki__id=pk)
        }
        return render(request, 'page-listing-grid.html', data)

class Pagedetailproduct(View):
    def get(self, request, pk):
        data = {
            'mahsulot': Mahsulot.objects.get(id=pk)
        }
        return render(request, 'page-detail-product.html', data)