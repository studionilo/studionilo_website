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
            payment.payer_email = request.POST['payer_email']
            payment.payer_id = request.POST['payer_id']
            payment.payer_status = request.POST['payer_status']
            payment.first_name = request.POST['first_name']
            payment.last_name = request.POST['last_name']
            payment.txn_id = request.POST['txn_id']
            payment.txn_type = request.POST['txn_type']
            payment.mc_currency = request.POST['mc_currency']
            payment.payment_fee = float(request.POST['payment_fee'])
            payment.payment_gross = float(request.POST['payment_gross'])
            payment.payment_revenue = payment.payment_gross - payment.payment_fee
            payment.payment_status = request.POST['payment_status']
            payment.payment_type = request.POST['payment_type']
            payment.item_name = request.POST['item_name']
            payment.payment_date = datetime.strptime(request.POST['payment_date'], '%Y-%m-%dT%H:%M:%SZ')
            payment.verify_sign = request.POST['verify_sign']

            payIntent = PaymentIntent.objects.filter(payment_intent_id=request.POST['custom']).first()
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

            return render(request, 'home/index.html', context=context)
        except:
            return redirect('home_reject')
    else:
        return redirect('homepage')

def reject(request):
    return render(request, 'home/index.html', context={'reject':True})

@csrf_exempt
def create_payment(request):
    if request.method == 'POST':
        try:
            payIntent = PaymentIntent()
            payIntent.name = request.POST['name']
            payIntent.email = request.POST['email'] 
            payIntent.website = request.POST['website']
            payIntent.sn_facebook = request.POST['sn_facebook'] == 'true'
            payIntent.sn_instagram = request.POST['sn_instagram'] == 'true'
            payIntent.sn_twitter = request.POST['sn_twitter'] == 'true'
            payIntent.sn_tiktok = request.POST['sn_tiktok'] == 'true'
            payIntent.sn_linkedin = request.POST['sn_linkedin'] == 'true'
            payIntent.sn_snapchat = request.POST['sn_snapchat'] == 'true'
            payIntent.sn_pinterest = request.POST['sn_pinterest'] == 'true'

            if(request.POST['plan'] == 'popup_pay_1'):
                payIntent.plan = PaymentIntent.VIDEOREPORT

            if(request.POST['plan'] == 'popup_pay_2'):
                payIntent.plan = PaymentIntent.VIDEOCOLLOQUIO

            if(request.POST['plan'] == 'popup_pay_3'):
                payIntent.plan = PaymentIntent.MEDIAMANAGER
            
            payIntent.screen_height = request.POST['screen_height']
            payIntent.screen_width = request.POST['screen_width']

            payIntent.user_agent = request.POST['user_agent']
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
            payIntent.payment_intent_id = '{:08d}_{}'.format(payIntent.pk, hash(request.session.session_key))
            payIntent.save()
            return JsonResponse({'payment_intent_id': payIntent.payment_intent_id})
        except:
            return JsonResponse({'error_message': traceback.format_exc()})
    else:
        return JsonResponse({'error_message': 'Used GET method instead of POST'})
