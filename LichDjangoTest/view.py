from django.http import HttpResponse
from django.shortcuts import render
import urllib.request


def index(request):
    context = {}
    return render(request, 'index.html', context)


def stars(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'stars.html', context)
    elif request.method == 'POST':
        context = {}
        # return render(request, 'index.html', context)

    response = urllib.request.urlopen('https://www.d1xz.net/yunshi/today/Gemini/')
    decode = response.read().decode()

    print(decode)
    return HttpResponse('ad')
