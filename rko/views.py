from django.shortcuts import render


# Create your views here.
def rko(request):
    return render(request, 'rko/rko.html')