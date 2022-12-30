# import os
from weasyprint import HTML, CSS

# GTK DLL dir path... for windows.
# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

# 'https://www.dip-badajoz.es/bop/boletin_completo.php?FechaSolicitada=2012-04-09'


def html_to_pdf():
    """
    Converts HTML to PDF
    """
    css = CSS(filename='style.css')
    HTML('test.html').write_pdf('weasygenerated.pdf',stylesheets=[css])


if __name__ == '__main__':
    html_to_pdf()
    