from django.contrib import admin
from .models import OrderItem, Order, Transaction

# admin.site.unregister(Schedule)


admin.site.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['schedule', 'is_ordered', 'date_added',
                    'date_ordered']
    list_filter = ['date_ordered']

admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['ref_code', 'owner', 'is_ordered', 'items',
                    'date_ordered']
    list_filter = ['date_ordered']

admin.site.register(Transaction)
class TransAdmin(admin.ModelAdmin):
    list_display = ['profile', 'token', 'order_id', 'amount',
                    'success', 'timestamp']
    list_filter = ['order_id']
