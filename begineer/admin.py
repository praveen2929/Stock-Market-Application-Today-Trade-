from django.contrib import admin
from begineer.models import course
# Register your models here.
class addAdmin1(admin.ModelAdmin):
    list_display=['title','desc','image1']

admin.site.register(course,addAdmin1)