import pdfkit
css = 'style.css'

options = {'header-html': 'header.html', 'footer-html': 'footer.html',}

pdfkit.from_file('template.html', 'wkpdftohtml_generated.pdf',css=css, options=options, verbose=True)
