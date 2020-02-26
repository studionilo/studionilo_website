from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PaymentIntent, Payment
import os
from user_agents import parse
import traceback
from datetime import datetime
import hashlib
from .niloemail import NiloEmail

def hash(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def home(request):
    return render(request, 'home/index.html')

def debugging(request):
    return render(request, 'home/index.html', context={'debugging':True})

@csrf_exempt
def awesome(request):
    if request.method == 'POST':
        try:
            payment = Payment()
            payment.payer_email = safe_post(request, 'payer_email')
            payment.payer_id = safe_post(request, 'payer_id')
            payment.payer_status = safe_post(request, 'payer_status')
            payment.first_name = safe_post(request, 'first_name')
            payment.last_name = safe_post(request, 'last_name')
            payment.txn_id = safe_post(request, 'txn_id')
            payment.txn_type = safe_post(request, 'txn_type')
            payment.mc_currency = safe_post(request, 'mc_currency')
            payment.payment_fee = float(safe_post(request, 'payment_fee'))
            payment.payment_gross = float(safe_post(request, 'payment_gross'))
            payment.payment_revenue = payment.payment_gross - payment.payment_fee
            payment.payment_status = safe_post(request, 'payment_status')
            payment.payment_type = safe_post(request, 'payment_type')
            payment.item_name = safe_post(request, 'item_name')
            payment.payment_date = datetime.strptime(safe_post(request, 'payment_date'), '%Y-%m-%dT%H:%M:%SZ')
            payment.verify_sign = safe_post(request, 'verify_sign')

            payIntent = PaymentIntent.objects.filter(payment_intent_id=safe_post(request, 'custom')).first()
            payIntent.purchased = True
            payIntent.save()

            payment.paymentIntent = PaymentIntent.objects.first()
            payment.save()
            if payIntent.plan == PaymentIntent.VIDEOREPORT:
                context={'awesome':'popup_pay_1'}
            elif payIntent.plan == PaymentIntent.VIDEOCOLLOQUIO:
                context={'awesome':'popup_pay_2'}
            else:
                context={'awesome':'popup_pay_3'}

            NiloEmail(payment.paymentIntent).send()
            return render(request, 'home/index.html', context=context)
        except:
            return redirect('home_reject')
    else:
        return redirect('homepage')

def reject(request):
    return render(request, 'home/index.html', context={'reject':True})

def safe_post(request, key, default=''):
    if key in request.POST:
        return request.POST[request, key]
    else:
        return default

@csrf_exempt
def create_payment(request):
    if request.method == 'POST':
        try:
            payIntent = PaymentIntent()
            payIntent.name = safe_post(request, 'name')
            payIntent.email = safe_post(request, 'email') 
            payIntent.website = safe_post(request, 'website')
            payIntent.sn_facebook = safe_post(request, 'sn_facebook') == 'true'
            payIntent.sn_instagram = safe_post(request, 'sn_instagram') == 'true'
            payIntent.sn_twitter = safe_post(request, 'sn_twitter') == 'true'
            payIntent.sn_tiktok = safe_post(request, 'sn_tiktok') == 'true'
            payIntent.sn_linkedin = safe_post(request, 'sn_linkedin') == 'true'
            payIntent.sn_snapchat = safe_post(request, 'sn_snapchat') == 'true'
            payIntent.sn_pinterest = safe_post(request, 'sn_pinterest') == 'true'

            if(safe_post(request, 'plan') == 'popup_pay_1'):
                payIntent.plan = PaymentIntent.VIDEOREPORT
            elif(safe_post(request, 'plan') == 'popup_pay_2'):
                payIntent.plan = PaymentIntent.VIDEOCOLLOQUIO
            elif(safe_post(request, 'plan') == 'popup_pay_3'):
                payIntent.plan = PaymentIntent.MEDIAMANAGER
            else:
                payIntent.plan = PaymentIntent.UNKNOWN

            
            payIntent.payment_intent_id = 'temporary_id'
            payIntent.save()
            payIntent.payment_intent_id = '{:08d}_{}'.format(payIntent.pk, hash(request.session.session_key))
            payIntent.save()
        except:
            return JsonResponse({'error_message': traceback.format_exc()})

        try:
            payIntent.screen_height = safe_post(request, 'screen_height')
            payIntent.screen_width = safe_post(request, 'screen_width')

            payIntent.user_agent = safe_post(request, 'user_agent')

            ua = parse(payIntent.user_agent)
            payIntent.browser_family = ua.browser.family
            payIntent.browser_version = ua.browser.version_string
            payIntent.os_family = ua.os.family
            payIntent.os_version = ua.os.version_string
            payIntent.device_family = ua.device.family
            payIntent.device_brand = ua.device.model
            payIntent.device_model = ua.device.brand
            payIntent.device_is_mobile = ua.is_mobile
            payIntent.device_is_tablet = ua.is_tablet
            payIntent.device_is_touch_capable = ua.is_touch_capable
            payIntent.device_is_pc = ua.is_pc
            payIntent.device_is_bot = ua.is_bot
            payIntent.save()
        except:
            pass

        NiloEmail(payIntent).send()
        return JsonResponse({'payment_intent_id': payIntent.payment_intent_id})
    else:
        return JsonResponse({'error_message': 'Used GET method instead of POST'})
