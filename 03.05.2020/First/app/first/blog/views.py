from django.shortcuts import render


def index(request):
    n = ['Aleksey', 'Duraley', 'Barmaley']
    return render(request, 'blog/index.html', context={'names': n})
