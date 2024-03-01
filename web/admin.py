from django.contrib import admin
from . models import Product
from . models import Contact
from . models import School
from . models import About
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(School)
admin.site.register(About)