from django.contrib import admin
from .models import Mahsulot_filter, Mahsulot, Oluvchi, Savdo, Chiqim

@admin.register(Mahsulot_filter)
class MahsulotFilterAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'filter', 'buy_price', 'sell_price', 'miqdori', 'izoh', 'time')
    list_filter = ('filter', 'time')

@admin.register(Oluvchi)
class OluvchiAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_number', 'total_cost', 'time')

@admin.register(Savdo)
class SavdoAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'cost', 'oluvchi')

@admin.register(Chiqim)
class ChiqimAdmin(admin.ModelAdmin):
    list_display = ('money', 'comment', 'person', 'date')
    list_filter = ('date',)

