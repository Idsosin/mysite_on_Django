from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def info(request):
    data = {
        'title': 'Наши контакты',
        'values': ['hello', 'Good day']
    }
    return render(request, 'main/info.html', data)