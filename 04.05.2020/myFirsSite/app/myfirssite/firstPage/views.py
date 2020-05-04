from django.shortcuts import render

def first(request):
    name = "World"
    return render(request, 'firstPage/index.html', context={"name": name})
