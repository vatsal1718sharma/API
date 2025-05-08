from django.contrib import admin
from apk.models import Order,OrderItem,CustomUser

# Register your models here.
class OrderIteminline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderIteminline,
    ]

admin.site.register(Order, OrderAdmin)
admin.site.register(CustomUser)