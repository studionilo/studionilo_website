from django.db import models

class PaymentIntent(models.Model):
    VIDEOREPORT = 'Video-report'
    VIDEOCOLLOQUIO = 'Video-colloquio'
    PIANOSUMISURA = 'Piano su misura'
    PAYMENTS = (
        (VIDEOREPORT, 'Video-report'),
        (VIDEOCOLLOQUIO, 'Video-colloquio'),
        (PIANOSUMISURA, 'Piano su misura'),
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
    session_key = models.CharField(max_length=32)
    purchased = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
