from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def submit(request):
    print(request.POST)
    return HttpResponse("Your Submit Sucess!!")