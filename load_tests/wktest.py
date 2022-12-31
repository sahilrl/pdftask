import pdfkit
css = 'style.css'


pdfkit.from_file('test.html', 'wkpdftohtml_generated.pdf', css=css)
