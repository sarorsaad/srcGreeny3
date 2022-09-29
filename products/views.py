from django.shortcuts import render
from django.views.generic import ListView,DetailView
from.models import Product, Brand,Category


# Create your list views here.
class ProductList(ListView):
      model = Product
class BrandList(ListView):
      model = Brand
class CategoryList(ListView):
      model = Category




# Create your detail views here.
class ProductDetail(DetailView):
     model = Product 