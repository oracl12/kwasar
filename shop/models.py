from django.db import models
from django.urls import reverse
from embed_video.fields  import  EmbedVideoField

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    #
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default=None)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default=None)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default=None)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default=None)
    #
    description = models.TextField(blank=True)
    title = models.TextField(blank=True)
    link_youtube = EmbedVideoField(blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'price')
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
