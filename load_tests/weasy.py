import os
from weasyprint import HTML

# GTK DLL dir path... for windows.
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")

# 'https://www.dip-badajoz.es/bop/boletin_completo.php?FechaSolicitada=2012-04-09'


def html_to_pdf():
    """
    Converts HTML to PDF
    """
    store = HTML('tables.html')
    document = store.render()
    # slice 0:2000 pages
    document.copy(document.pages[0:2000]).write_pdf('odd_pages.pdf')


if __name__ == '__main__':
    html_to_pdf()
