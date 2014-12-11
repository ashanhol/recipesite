from django.shortcuts import render

# Create your views here.


def about_view(request):
    return render(request, 'home/about.html')

def home_view(request):
    return render(request, 'home/index.html')
