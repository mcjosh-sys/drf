from django.conf import settings
from django.db import models
import random

User = settings.AUTH_USER_MODEL
# Create your models here.
TAGS_MODEL_VALUES = ['magic','books','stones','alchemy']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = models.Q(title__icontains=query) | models.Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs_2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs_2).distinct()
        return qs
    
class ProductManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
    
    def search(self, query, user=None):
        return self.get_queryset().search(query)

class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)
    
    objects = ProductManager()
    
    def is_public(self):
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    def get_discount(self):
        return "%.2f" %(float(self.price)*0.22)