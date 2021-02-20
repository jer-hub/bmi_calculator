from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'bmi/home.html')

def result(request):
    height = float(request.GET.get('height',1))
    weight = float(request.GET.get('weight',1))

    bmi = float(weight/(height**2))
    return render(request, 'bmi/result.html', {
        'thebmi' : bmi
    })