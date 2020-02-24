from django.contrib import admin
from .models import PaymentIntent, Payment

class PaymentIntentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'email', 
        'website', 
        'plan',
        'sn_facebook', 
        'sn_instagram', 
        'sn_twitter', 
        'sn_tiktok', 
        'sn_linkedin', 
        'sn_snapchat',
        'sn_pinterest',
        'purchased',
        'date',
        )
    list_filter = (
        'date',
        'purchased',
        'plan',
        )

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payer_email', 
        'first_name', 
        'last_name',
        'item_name', 
        'payment_status', 
        'mc_currency',
        'payment_fee',
        'payment_gross',
        'payment_revenue',
        'payment_date', 
        'paymentIntent', 
        )
    list_filter = (
        'payment_date',
        'payment_status',
        'item_name',
        )

admin.site.register(PaymentIntent, PaymentIntentAdmin)
admin.site.register(Payment, PaymentAdmin)
