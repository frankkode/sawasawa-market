from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import Job


# Create your views here.
def job_index(request):
    jobbs = Job.objects.all()
    context = {'jobbs': jobbs}
    template_name = 'job_index.html'  
    context_object_name = 'jobbs'
    return render(request, 'job_index.html', context)


def job_detail(request, id):
    
    jobb = get_object_or_404(Job, id=id)
    context = {'jobb': jobb}
    template_name = 'job_detail.html'
    return HttpResponse(render(request, 'job_detail.html', context))


 