from django.shortcuts import render


# Create your views here.
def debit(request):
    return render(request, 'debit/debit.html')