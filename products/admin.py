from django.contrib import admin
from .models import Product,Brand,Category
from .models import ProductImages,ProductReview
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# class ProductAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     summernote_fields = '__all__'


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)


admin.site.register(ProductReview)
admin.site.register(ProductImages)