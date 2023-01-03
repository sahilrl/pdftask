# import os
from weasyprint import HTML, CSS

# GTK DLL dir path... for windows.
# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

# 'https://www.dip-badajoz.es/bop/boletin_completo.php?FechaSolicitada=2012-04-09'


def html_to_pdf(template, css):
    """
    Converts HTML to PDF
    """
    css = CSS(filename=css)
    return HTML(string=template).write_pdf(stylesheets=[css])
