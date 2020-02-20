from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PaymentIntent
import os

# stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
# stripe.api_version = os.getenv('STRIPE_API_VERSION')

def home(request):
    return render(request, 'home/index.html')

def awesome(request):
    payIntent = PaymentIntent.objects.filter(session_key=request.session.session_key).first()
    if not payIntent is None:
        payIntent.purchased = True
        payIntent.save()
    return render(request, 'home/index.html', context={'awesome':'popup_pay_1'})

def reject(request):
    return render(request, 'home/index.html')

@csrf_exempt
def create_payment(request):
    if request.method == 'POST':
        try:
            payIntent = PaymentIntent.objects.filter(session_key=request.session.session_key, purchased=False).first()
            if payIntent is None:
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
                payIntent.plan = PaymentIntent.PIANOSUMISURA

            payIntent.session_key = request.session.session_key
            payIntent.save()
            return JsonResponse({'primary_key': payIntent.pk, 'session_key': request.session.session_key})
        except:
            return JsonResponse({'primary_key': False})
    else:
        return JsonResponse({'primary_key': False})

# @csrf_exempt
# def create_payment(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         # Create a PaymentIntent with the order amount and currency
#         intent = stripe.PaymentIntent.create(
#             amount=1000,
#             currency=data['currency']
#         )

#         try:
#             # Send publishable key and PaymentIntent details to client
#             return HttpResponse(json.dumps({'publishableKey': os.getenv('STRIPE_PUBLISHABLE_KEY'), 'clientSecret': intent.client_secret}))
#         except Exception as e:
#             return HttpResponse(json.dumps(error=str(e)), status=403)
#     else:
#             return HttpResponse(json.dumps({'message': 'POST request needed'}), status=400)

# @csrf_exempt
# def webhook_received():
#     if request.method == 'POST':
#         # You can use webhooks to receive information about asynchronous payment events.
#         # For more about our webhook events check out https://stripe.com/docs/webhooks.
#         webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
#         request_data = json.loads(request.body)

#         if webhook_secret:
#             # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
#             signature = request.headers.get('stripe-signature')
#             try:
#                 event = stripe.Webhook.construct_event(
#                     payload=request.data, sig_header=signature, secret=webhook_secret)
#                 data = event['data']
#             except Exception as e:
#                 return e
#             # Get the type of webhook event sent - used to check the status of PaymentIntents.
#             event_type = event['type']
#         else:
#             data = request_data['data']
#             event_type = request_data['type']
#         data_object = data['object']

#         if event_type == 'payment_intent.succeeded':
#             print('💰 Payment received!')
#             # Fulfill any orders, e-mail receipts, etc
#             # To cancel the payment you will need to issue a Refund (https://stripe.com/docs/api/refunds)
#         elif event_type == 'payment_intent.payment_failed':
#             print('❌ Payment failed.')
#         return HttpResponse(json.dumps({'status': 'success'}))
#     else:
#         return HttpResponse(json.dumps({'message': 'POST request needed'}), status=400)
