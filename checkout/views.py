import stripe # new

from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect # new
from django import forms

stripe.api_key = settings.STRIPE_SECRET_KEY # new


class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=2000,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )

    #return render(request, 'blog/post_form.html')
    return render(request, 'charge.html')
    
    
        




