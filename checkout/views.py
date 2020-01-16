from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import stripe
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY



@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=1000,
                currency='sek',
                source=token,
                description='Example charge',
                
                
                )
        except stripe.error.CardError as e:
            message.info(request, "Your card has been declined.")
        
    context = {'publishKey':publishKey}
    templete = 'checkout.html'
    return render(request, templete, context)
    

def pay_success(request, **kwargs):
    return HttpResponseRedirect('/blog-success/')
    #return render('blog/pay_success.html')






    