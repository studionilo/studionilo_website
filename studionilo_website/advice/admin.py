from django.contrib import admin
from .models import PaymentIntent, Payment

def mark_as_done(modeladmin, request, queryset):
    queryset.update(done=True)
mark_as_done.short_description = "Mark selected as done"

def mark_as_to_do(modeladmin, request, queryset):
    queryset.update(done=False)
mark_as_to_do.short_description = "Mark selected as to-do"
class PaymentIntentAdmin(admin.ModelAdmin):
    list_display = [
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
        'done',
    ]
    list_filter = [
        'date',
        'purchased',
        'plan',
        'done',
        ]
    actions = [
        mark_as_done,
        mark_as_to_do,
    ]

class PaymentAdmin(admin.ModelAdmin):
    list_display = [
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
    ]
    list_filter = [
        'payment_date',
        'payment_status',
        'item_name',
    ]

admin.site.register(PaymentIntent, PaymentIntentAdmin)
admin.site.register(Payment, PaymentAdmin)
