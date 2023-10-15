from lxml import html, etree
import aspose.cells
from aspose.cells import Workbook, FileFormatType

file = "input2.html"

with open(file, 'r', encoding='utf-8') as inp: 
    htmldoc = html.fromstring(inp.read())

with open("output2.xml", 'wb') as out: 
    out.write(etree.tostring(htmldoc))

workbook = Workbook("output2.xml")
workbook.save("output_htmltodocx.docx")

# workbook = Workbook("input2.html")
# workbook.save("output_html_to_docx2.docx")