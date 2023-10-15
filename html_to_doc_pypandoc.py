# import pypandoc.convert
# output = pypandoc.convert(source='input2.html', format='html', to='docx', outputfile='outputof_pypandoc.docx', extra_args=['-RTS'])

from htmldocx import HtmlToDocx

new_parser = HtmlToDocx()
new_parser.parse_html_file("input2.html", "htmldocx.docx")