from django.shortcuts import render

# Create your views here.

def home(request):

    height = float(request.GET.get('height',1))
    weight = float(request.GET.get('weight',2))

    bmi = float(weight/(height**2))

    return render(request, 'bmi/home.html', {
        'thebmi' : bmi
    })

def result(request):
    return render(request, 'bmi/result.html')