# coding=UTF-8

"""
Definition of models.
"""

from django.db import models

# Create your models here.
class ProductCategory (models.Model):
    code = models.CharField (max_length = 2, primary_key = True)
    name = models.CharField (max_length = 10)
    name_indo = models.CharField (max_length = 50, blank = True)
    name_viet = models.CharField (max_length = 50, blank = True)
    show_it = models.BooleanField (default = True)
    created_date = models.DateTimeField (auto_now_add=True)
    last_modify_time = models.DateTimeField (auto_now =  True, auto_now_add = True)

    def __str__ (self):
        return self.name

class UOM (models.Model):
    name = models.CharField (max_length = 10)
    name_indo = models.CharField (max_length = 20, blank = True)
    name_viet = models.CharField (max_length = 20, blank = True)
    created_date = models.DateTimeField (auto_now_add=True)
    last_modify_time = models.DateTimeField (auto_now =  True, auto_now_add = True)

    def __str__ (self):
        return self.name

class Product (models.Model):
    code = models.CharField (max_length = 6, primary_key = True)
    category = models.ForeignKey (ProductCategory)
    name = models.CharField (max_length = 50)
    name_indo = models.CharField (max_length = 100, blank = True)
    name_viet = models.CharField (max_length = 100, blank = True)
    spec = models.CharField (max_length = 50, blank = True)
    uom = models.ForeignKey (UOM)
    sale_price = models.FloatField ()
    is_active = models.BooleanField (default = True)
    sales_intro = models.TextField (blank = True)
    sales_intro_indo = models.TextField (blank = True)
    sales_intro_viet = models.TextField (blank = True)
    sort_order = models.IntegerField (default = 0)
    # use predefined image path first
    #pic_master = models.ImageField ()
    #pic_1 = models.ImageField ()
    #pic_2 = models.ImageField ()
    #pic_3 = models.ImageField ()
    created_date = models.DateTimeField (auto_now_add = True, blank = True)
    last_modify_time = models.DateTimeField (auto_now = True, auto_now_add = True)

    def  __str__ (self):
        return self.name