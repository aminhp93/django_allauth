
from django.contrib import admin


from .models import Cart, CartItem
# Register your models here.

class CartItemInline(admin.TabularInline):
	model = CartItem



class CartAdmin(admin.ModelAdmin):
	inlines = [CartItemInline]
	class Meta:
		model = Cart

admin.site.register(Cart, CartAdmin)
