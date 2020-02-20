from django.contrib import admin
from .models import PaymentIntent

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
        'session_key',
        'date',
        )
    list_filter = (
        'date',
        'purchased',
        'plan',
        )

admin.site.register(PaymentIntent, PaymentIntentAdmin)
