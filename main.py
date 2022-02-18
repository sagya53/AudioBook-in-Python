import pyttsx3
import PyPDF2
book = open("oop.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
pageNo = int(input("Enter The Page Number You Want To Read It :  "))
no = pageNo
for num in range(no, pages):
    page = pdfReader.getPage(no)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()