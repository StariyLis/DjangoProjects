from django.shortcuts import render

def first(request):
    return render(request, 'firstPage/index.html')
