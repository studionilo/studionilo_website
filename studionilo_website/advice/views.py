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
import os,binascii
from django.contrib.admin.views.decorators import staff_member_required

def hash(value):
    if not value is None:
        return hashlib.sha256(value.encode('utf-8')).hexdigest()
    else:
        return hashlib.sha256('none'.encode('utf-8')).hexdigest()

def home(request):
    return render(request, 'advice/advice.html')

@csrf_exempt
def awesome(request):
    if request.method == 'POST':
        try:
            payment = Payment()
            payment.payer_email = request.POST.get('payer_email', '')
            payment.payer_id = request.POST.get('payer_id', '')
            payment.payer_status = request.POST.get('payer_status', '')
            payment.first_name = request.POST.get('first_name', '')
            payment.last_name = request.POST.get('last_name', '')
            payment.txn_id = request.POST.get('txn_id', '')
            payment.txn_type = request.POST.get('txn_type', '')
            payment.mc_currency = request.POST.get('mc_currency', '')
            payment.payment_fee = float(request.POST.get('payment_fee', ''))
            payment.payment_gross = float(request.POST.get('payment_gross', ''))
            payment.payment_revenue = payment.payment_gross - payment.payment_fee
            payment.payment_status = request.POST.get('payment_status', '')
            payment.payment_type = request.POST.get('payment_type', '')
            payment.item_name = request.POST.get('item_name', '')
            payment.payment_date = datetime.strptime(request.POST.get('payment_date', ''), '%Y-%m-%dT%H:%M:%SZ')
            payment.verify_sign = request.POST.get('verify_sign', '')

            payIntent = PaymentIntent.objects.filter(payment_intent_id=request.POST.get('custom', '')).first()
            if not payIntent is None:
                payIntent.purchased = True
                payIntent.save()
                payment.paymentIntent = PaymentIntent.objects.first()
            payment.save()
            
            context={}
            if payIntent.plan == PaymentIntent.VIDEOCOLLOQUIO:
                context={'awesome':'videocall'}

            NiloEmail(payment.paymentIntent).send()
            return render(request, 'advice/advice.html', context=context)
        except:
            raise
            return redirect('advice_reject')
    else:
        return redirect('advice_home')

def reject(request):
    return render(request, 'advice/advice.html', context={'reject':'videocall'})

@csrf_exempt
def create_payment(request):
    if request.method == 'POST':
        try:
            payIntent = PaymentIntent()
            payIntent.name = request.POST.get('name', '')
            payIntent.email = request.POST.get('email', '') 
            payIntent.website = request.POST.get('website', '')
            payIntent.sn_facebook = request.POST.get('sn_facebook', '') == 'true'
            payIntent.sn_instagram = request.POST.get('sn_instagram', '') == 'true'
            payIntent.sn_twitter = request.POST.get('sn_twitter', '') == 'true'
            payIntent.sn_tiktok = request.POST.get('sn_tiktok', '') == 'true'
            payIntent.sn_linkedin = request.POST.get('sn_linkedin', '') == 'true'
            payIntent.sn_snapchat = request.POST.get('sn_snapchat', '') == 'true'
            payIntent.sn_pinterest = request.POST.get('sn_pinterest', '') == 'true'

            if(request.POST.get('plan', '') == 'videoreport'):
                payIntent.plan = PaymentIntent.VIDEOREPORT
            elif(request.POST.get('plan', '') == 'videocall'):
                payIntent.plan = PaymentIntent.VIDEOCOLLOQUIO
            elif(request.POST.get('plan', '') == 'managing'):
                payIntent.plan = PaymentIntent.MEDIAMANAGER
            elif(request.POST.get('plan', '') == 'website'):
                payIntent.plan = PaymentIntent.WEBSITE
            else:
                payIntent.plan = PaymentIntent.UNKNOWN

            tmp_id = 'temporary_id_{}'.format(binascii.b2a_hex(os.urandom(4)))
            while(not PaymentIntent.objects.filter(payment_intent_id=tmp_id).first() is None):
                tmp_id = 'temporary_id_{}'.format(binascii.b2a_hex(os.urandom(20)))

            payIntent.payment_intent_id = tmp_id
            payIntent.save()
            payIntent.payment_intent_id = '{:08d}_{}'.format(payIntent.pk, hash(request.session.session_key))
            payIntent.save()
        except:
            return JsonResponse({'error_message': traceback.format_exc()})

        try:
            payIntent.screen_height = request.POST.get('screen_height', '')
            payIntent.screen_width = request.POST.get('screen_width', '')

            payIntent.user_agent = request.POST.get('user_agent', '')
            if len(payIntent.user_agent) > 0:
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
        
        try:
            if payIntent.plan == PaymentIntent.MEDIAMANAGER:
                NiloEmail(payIntent).send()
        except:
            pass
        return JsonResponse({'payment_intent_id': payIntent.payment_intent_id})
    else:
        return JsonResponse({'error_message': 'Used GET method instead of POST'})