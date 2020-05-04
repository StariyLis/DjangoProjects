from django.shortcuts import render

def first(request):
    return render(request, 'firstPage/first.html')


def blog(request):
    return render(request, 'firstPage/blog.html')


def about(request):
    return render(request, 'firstPage/about.html')
