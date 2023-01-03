from django.shortcuts import render
from django.http import HttpResponse
from .weasy import html_to_pdf
from django.conf import settings
from django.template.loader import get_template


def home(request):
    """
    HomePage
    """
    return render(request, 'report.html', {'n':10, 'foot': 0})


def report1(request):
    """
    Download Portrait PDF
    """
    css = settings.BASE_DIR.joinpath('static/css/printportrait.css')
    template = get_template('report.html').render({'n': 10, 'foot': 1, 'request': request})
    filebyte = html_to_pdf(template, css)
    return HttpResponse(filebyte, headers = {
                        'Content-Type': 'application/pdf',
                        'Content-Disposition': 'attachment; filename="reportportrait.pdf"',
                        } )
    

def report2(request):
    """
    Download Landscape PDF
    """
    css = settings.BASE_DIR.joinpath('static/css/printlandscape.css')
    template = get_template('report.html').render({'n': 10, 'foot': 1, 'request': request})
    filebyte = html_to_pdf(template, css)
    return HttpResponse(filebyte, headers = {
                        'Content-Type': 'application/pdf',
                        'Content-Disposition': 'attachment; filename="reportlandscape.pdf"',
                        } )