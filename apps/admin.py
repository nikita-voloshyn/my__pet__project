from django.contrib import admin
from .models import User, Category, Product, Order, OrderDetail

# Кастомная админка для пользователя, если требуется
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'is_active', 'is_admin']
    search_fields = ['email', 'username']
    list_filter = ['is_admin', 'is_active']

admin.site.register(User, UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category']
    search_fields = ['name', 'category__name']
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'creation_date', 'status']
    search_fields = ['user__username', 'status']
    list_filter = ['status', 'creation_date']

admin.site.register(Order, OrderAdmin)

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'unit_price']
    search_fields = ['order__id', 'product__name']

admin.site.register(OrderDetail, OrderDetailAdmin)
