from django.urls import path
from . import views as home_views

urlpatterns = [
    path('', home_views.home, name='homepage'),
    path('debugging', home_views.debugging, name='home_debuggin'),
    path('fantastico', home_views.awesome, name='home_awesome'),
    path('ops', home_views.reject, name='home_reject'),
    path('api/create-payment-intent', home_views.create_payment),
    # path('webhook', home_views.webhook_received),
]