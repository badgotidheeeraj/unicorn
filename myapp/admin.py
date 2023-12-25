from django.contrib import admin
from .models import practis 

# Register your models here.
# admin.site.register(practis)
class register(admin.ModelAdmin):
     list_display=['id','name','compony','address','pin']






admin.site.register( practis,register)