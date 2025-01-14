from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = (
        'address', 'price', 'new_building', 'construction_year',
        'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    readonly_fields = ('pure_phone',)
    raw_id_fields = ('flat',)
    fields = ('name', 'phone', 'pure_phone', 'flat', )
