from django.contrib import admin
from account.models import person
from account.models import notification
# Register your models here.
class addAdmin(admin.ModelAdmin):
    list_display=['fname','lname','number','email','date_of_birth','State','city','password','isactive']

admin.site.register(person,addAdmin)
class addNotification(admin.ModelAdmin):
    list_display=['notification']

admin.site.register(notification,addNotification)