from django.shortcuts import render
# from .read import mapo_name
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

