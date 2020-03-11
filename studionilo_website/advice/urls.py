from django.urls import path
from . import views as advice_views

urlpatterns = [
    path('', advice_views.home, name='homepage'),
    path('fantastico', advice_views.awesome, name='advice_awesome'),
    path('ops', advice_views.reject, name='advice_reject'),
    path('api/create-payment-intent', advice_views.create_payment),
]