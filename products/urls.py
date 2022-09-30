from django.urls import path
from .views import ProductList,BrandList,CategoryList
#-----------------------------------------
from .views import ProductDetail,BrandDetail

app_name='products'

urlpatterns = [
 path("", ProductList.as_view(), name="product_list"),  
 path("brands/", BrandList.as_view(), name="brand_list"),
 path("category/", CategoryList.as_view(), name="category_List"),

# deatail urls
 path("<pk>/", ProductDetail.as_view(), name="product_detail"),
 path("brands/<int:pk>", BrandDetail.as_view(), name="brand_detail"),
]