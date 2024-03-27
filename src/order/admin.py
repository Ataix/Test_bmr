from django.contrib import admin

from .models import Order


class OrderItemInline(admin.TabularInline):
    model = Order.items.through
    fields = ['product', 'quantity', 'price']
    readonly_fields = ['product', 'quantity', 'price']
    extra = 0

    def product(self, instance):
        return instance.orderitems

    def quantity(self, instance):
        return instance.orderitems.quantity

    def price(self, instance):
        return instance.orderitems.price


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
