from django.shortcuts import render


def hello(request):
    name = request.GET['name']
    message = request.GET['message']

    content = {
        'name': name,
        'message': message
    }
    return render(request, 'base.html', content)


def helloRekruto(request):
    return render(request, 'helloRekruto.html')
