from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'), # new
    #path('', views.HomePageView.as_view(), name='home'),
    #path('checkout/', checkout_views.checkout, name='checkout'),
    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),
]