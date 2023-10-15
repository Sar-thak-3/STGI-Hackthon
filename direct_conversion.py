import win32com.client

word = win32com.client.Dispatch('Word.Application')

word.Visible = True

word.Documents.Open('input.html')
word.ActiveDocument.ActiveWindow.View.Type = 3

word.ActiveDocument.SaveAs("ou.docx")
word.Quit()