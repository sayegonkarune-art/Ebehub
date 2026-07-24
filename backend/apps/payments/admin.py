from django.contrib import admin
from .models import Payment, Refund, Invoice

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'order', 'amount', 'payment_method', 'status', 'created_at']
    list_filter = ['payment_method', 'status', 'created_at']
    search_fields = ['transaction_id', 'order__order_number']
    readonly_fields = ['transaction_id', 'created_at', 'updated_at']

@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment', 'amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'order', 'amount', 'issued_at', 'paid_at']
    list_filter = ['issued_at', 'paid_at']
    search_fields = ['invoice_number', 'order__order_number']
    readonly_fields = ['invoice_number', 'issued_at']
