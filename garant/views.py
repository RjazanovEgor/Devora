from django.shortcuts import render


# Create your views here.
def garant(request):
    return render(request, 'garant/garant.html')