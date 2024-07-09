from django.contrib import admin
from investor.models import course
# Register your models here.
class addAdmin(admin.ModelAdmin):
    list_display=['title','desc','image1']

admin.site.register(course,addAdmin)