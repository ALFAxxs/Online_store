from django.contrib import admin
from .models import Catergory, Item

admin.site.register(Catergory) #1-way to register model
admin.site.register(Item)

# @admin.register(Catergory)  #2-way to register model
# class CategoryAdmin(admin.ModelAdmin):
#     pass
# # Register your models here.
