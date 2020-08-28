from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)               #null -> nullable on DB
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='This is great summary', blank=False, null=False)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('products:product_detail_view', kwargs={'product_id': self.id})
