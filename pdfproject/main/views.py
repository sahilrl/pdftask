from django.shortcuts import render
from django.http import HttpResponse


def report(request):
    return render(request, 'report.html', {'n': 100})
