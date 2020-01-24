from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import Car


# Create your views here.
def car_index(request):
    cars = Car.objects.all()
    context = {'cars': cars}

    template_name = 'car_index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'cars'
    return render(request, 'car_index.html', context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    context = {'car': car}
    template_name = 'car_detail.html'
    return HttpResponse(render(request, 'car_detail.html', context))

