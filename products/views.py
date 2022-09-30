from django.shortcuts import render
from django.views.generic import ListView,DetailView
from.models import Product, Brand,Category
from.models import ProductImages
from django.db.models import Count

# Create your list views here.
class ProductList(ListView):
      model = Product
#------------------------
class BrandList(ListView):
      model = Brand
      
      def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)  
        context["brands"] = Brand.objects.all().annotate(product_count=Count('product_brand'))       
        return context
  
class BrandDetail(DetailView):
      model = Brand

      def get_context_data(self,  **kwargs):
        context = super().get_context_data( **kwargs)
        brand=self.get_object()  
        context["brand_products"] = Product.objects.filter(brand=brand)       
        return context


#------------------------

class CategoryList(ListView):
      model = Category




# Create your detail views here.
class ProductDetail(DetailView):
     model = Product
     

     def get_context_data(self, **kwargs):
        context = super().get_context_data( **kwargs)
        myproduct=self.get_object() 
        context["images"] = ProductImages.objects.filter(product=myproduct)
        context["related"] = Product.objects.filter(category=myproduct.category)         
        return context