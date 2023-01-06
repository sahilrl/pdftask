from django.shortcuts import render
from django.http import HttpResponse
from .weasy import html_to_pdf
from django.conf import settings
from django.template.loader import get_template


def home(request):
    """
    HomePage
    """
    return render(request, 'report.html', {'n':10, 'display_running_elements': 0})


def report(request):
    """
    Download Portrait PDF and Landscape PDF
    """
    if request.path == '/report1/':
        css = settings.BASE_DIR.joinpath('static/css/printportrait.css')
        filename = 'reportportrait.pdf'
   
    if request.path == '/report2/':
        css = settings.BASE_DIR.joinpath('static/css/printlandscape.css')
        filename = 'reportlandscape.pdf'

    template = get_template('report.html').render({'n': 10, 'display_running_elements': 1, 'request': request})
    filebyte = html_to_pdf(template, css)
    return HttpResponse(filebyte, headers = {
                        'Content-Type': 'application/pdf',
                        'Content-Disposition': f'attachment; filename={filename}',
                        } )
