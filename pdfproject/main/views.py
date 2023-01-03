from django.shortcuts import render
from django.http import HttpResponse
from .weasy import html_to_pdf
from django.conf import settings
from django.template.loader import get_template
# from django.http import FileResponse

template = get_template('report.html').render({'n': 10, 'foot': 1})

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
    filebyte = html_to_pdf(template, css)
    mime_type = 'application/pdf'
    response = HttpResponse(filebyte, headers = {
                            'Content-Type': mime_type,
                            'Content-Disposition': 'attachment; filename="report.pdf"',
                            } )
    return response
    

def report2(request):
    """
    Download Landscape PDF
    """
    css = settings.BASE_DIR.joinpath('static/css/printlandscape.css')
    html_to_pdf(template, css)
    return HttpResponse('landscape pdf downloaded successfuly')