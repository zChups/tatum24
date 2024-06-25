from django.shortcuts import render


def HomeView(request):
    return render(request, 'tatum24/templates/home.html')
