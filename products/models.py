from django.db import models
from django.utils.translation import gettext as _
from django.utils import  timezone
from django.contrib.auth.models import User


PRODUCT_FLAG=(
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale')

)

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=30)
    sku=models.IntegerField(_('SKU'), null=True)
    subtitle = models.CharField(_('Subtitle '),max_length=30, null=True)
    desc = models.TextField(_('Description '),max_length=30, null=True)
    flag = models.CharField(_('Flag'), max_length = 10,choices=PRODUCT_FLAG, null=True)
    price=models.FloatField(_('Price'), null=True)
    image=models.ImageField( upload_to='products', null=True)
    # tags=TaggableManger()
    category=models.ForeignKey('Category',verbose_name=_('Category'), related_name='product_category' ,on_delete= models.SET_NULL,null=True,blank=True)
    
    brand= models.ForeignKey('Brand',verbose_name=_('Brand'), related_name='product_brand' ,on_delete= models.SET_NULL,null=True,blank=True)
    video_url=models.URLField(null=True,blank=True)
    def __str__(self):
        return (self.name)

class ProductImages(models.Model):
    product = models.ForeignKey('Product', verbose_name= _('Product'), related_name='product_image' ,on_delete= models.CASCADE)
    image=models.ImageField(verbose_name= _('Image'), upload_to='productimages', null=True)
    def __str__(self):
        return str(self.product)
class Brand(models.Model):
     name = models.CharField(_('Name'), max_length=30)
     image = models.ImageField(_('Image'),upload_to="brand", null=True)
     def __str__(self):
        return (self.name)
class Category(models.Model):
    # Fields
    image = models.ImageField(_('Image'),upload_to="category" , null=True)
    name = models.CharField(_('Name'),max_length=100)

    def __str__(self):
        return (self.name)   
class ProductReview(models.Model):
    user = models.ForeignKey(User,  related_name='user_review' ,on_delete=  models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product, verbose_name= _('Product'), related_name='product_review' ,on_delete=  models.SET_NULL,null=True,blank=True)
    rate=models.IntegerField(_('Rate'))
    review = models.CharField(_('Review'), max_length=300)
    created_at=models.DateField(default=timezone.now)
    def __str__(self):
        return str(self.product)
