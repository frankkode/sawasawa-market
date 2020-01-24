from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import House


# Create your views here.
def house_index(request):
    houses = House.objects.all()
    context = {'houses': houses}

    template_name = 'house_index.html'  
    context_object_name = 'houses'
    return render(request, 'house_index.html', context)


def house_detail(request, id):
    
    house = get_object_or_404(House, id=id)
    context = {'house': house}
    template_name = 'house_detail.html'
    return HttpResponse(render(request, 'house_detail.html', context))

