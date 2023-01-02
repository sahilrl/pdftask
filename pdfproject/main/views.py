from django.shortcuts import render
from django.http import HttpResponse
from .weasy import html_to_pdf
from django.conf import settings
from django.template.loader import get_template


def report(request):
    css = settings.STATIC_ROOT + 'css/print.css'
    print('before template')
    template = get_template('report.html').render({'n': 500})
    print('started')
    html_to_pdf(template, css)
    return HttpResponse('ok')
