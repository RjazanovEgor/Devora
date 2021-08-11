from django.shortcuts import render


# Create your views here.
def credit(request):
    return render(request, 'credit/credit.html')