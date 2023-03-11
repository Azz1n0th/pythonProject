from django.contrib import admin
from .models import *


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(PhysicalProduct)
class PhysicalProduct(admin.ModelAdmin):
    pass


@admin.register(ServiceProduct)
class ServiceProductAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceInbound)
class InvoiceInboundAdmin(admin.ModelAdmin):
    pass


@admin.register(InvoiceOutbound)
class InvoiceOutboundAdmin(admin.ModelAdmin):
    pass


@admin.register(FiscalNote)
class FiscalNoteAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessAccount)
class AccessAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Vendors)
class VendorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    pass


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    pass


@admin.register(ExpenseItem)
class ExpenseItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    pass

