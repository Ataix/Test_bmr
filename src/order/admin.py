from django.contrib import admin

from .models import Order


class OrderItemInline(admin.TabularInline):
    model = Order.items.through
    fields = [
        'product',
        'quantity',
        'price',
        'discount',
    ]


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = (
        'user',
        'created_at',
        'address',
        'comment',
        'total',
        'discount',
    )


admin.site.register(Order, OrderAdmin)
