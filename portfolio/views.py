from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Contact

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def submit(request):
    if(request.method == "POST"):
        contact = Contact()
        contact.name = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.msg = request.POST.get("message")
        contact.save()
        return HttpResponse(status=200)
    return HttpResponse(status=404)