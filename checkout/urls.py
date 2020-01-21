from django.urls import path


from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'), # new
    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),
]