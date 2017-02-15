from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available','created','updated']
    """
    Any field in list_editable must also be listed in the list_display attribute, since
    only the fields displayed can be edited.
    """
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product, ProductAdmin)    
