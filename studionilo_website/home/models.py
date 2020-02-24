from django.db import models

class PaymentIntent(models.Model):
    VIDEOREPORT = 'Video-report'
    VIDEOCOLLOQUIO = 'Video-colloquio'
    MEDIAMANAGER = 'Social media manager'
    PAYMENTS = (
        (VIDEOREPORT, 'Video-report'),
        (VIDEOCOLLOQUIO, 'Video-colloquio'),
        (MEDIAMANAGER, 'Social media manager'),
    )
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    website = models.CharField(max_length=256)
    plan = models.CharField(max_length=25, default=VIDEOREPORT, choices=PAYMENTS)
    sn_facebook = models.BooleanField(default=False)
    sn_instagram = models.BooleanField(default=False)
    sn_twitter = models.BooleanField(default=False)
    sn_tiktok = models.BooleanField(default=False)
    sn_linkedin = models.BooleanField(default=False)
    sn_snapchat = models.BooleanField(default=False)
    sn_pinterest = models.BooleanField(default=False)
    # sn_other = models.CharField(max_length=256, default='')
    payment_intent_id = models.CharField(max_length=256, default='', unique=True)
    purchased = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    user_agent = models.TextField(null=True)
    browser_family = models.CharField(max_length=128, null=True)
    browser_version = models.CharField(max_length=32, null=True)
    os_family = models.CharField(max_length=128, null=True)
    os_version = models.CharField(max_length=32, null=True)
    device_family = models.CharField(max_length=128, null=True)
    device_brand = models.CharField(max_length=128, null=True)
    device_model = models.CharField(max_length=128, null=True)
    screen_height = models.IntegerField(null=True)
    screen_width = models.IntegerField(null=True)
    device_is_mobile = models.BooleanField(default=False)
    device_is_tablet = models.BooleanField(default=False)
    device_is_touch_capable = models.BooleanField(default=False)
    device_is_pc = models.BooleanField(default=False)
    device_is_bot = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Payment(models.Model):
    payer_email = models.CharField(max_length=256)
    payer_id = models.CharField(max_length=256)
    payer_status = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    txn_id = models.CharField(max_length=256, unique=True)
    txn_type = models.CharField(max_length=256)
    mc_currency = models.CharField(max_length=256)
    payment_fee = models.FloatField()
    payment_gross = models.FloatField()
    payment_revenue = models.FloatField()
    payment_status = models.CharField(max_length=256)
    payment_type = models.CharField(max_length=256)
    item_name = models.CharField(max_length=256)
    payment_date = models.DateTimeField()
    verify_sign = models.CharField(max_length=256)

    paymentIntent = models.ForeignKey(PaymentIntent, on_delete = models.CASCADE) 

    def __str__(self):
        return self.payer_email

