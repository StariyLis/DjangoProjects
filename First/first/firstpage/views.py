from django.shortcuts import render

def first(request):
    n = 'Aleksey'
    return render(request, 'firstpage/firstpage-base.html', context={'name': n})
