import PyPDF2
import csv
import pandas as pd

# parse Special Districts1-56-89-2829-33 & 49-545 STEPPING STONE LN GREAT NECK3 STEPPING STONE LN GREAT NECK2 ELM PL GREAT NECK50 KINGS POINT RD GREAT NECK251 STEAMBOAT RD GREAT NECK
def parsePageText(textInput):
    addresses = []
    #print(text)
    validStr = ""
    result = text.find("Special Districts")
    for i in range(result + len("Special Districts"), len(text)):
        if text[i] == '.':
            break
        validStr += text[i]

    #print(validStr)
    address = ""
    prevChar = False
    for c in validStr:
        if c.isdigit() and prevChar:
            if len(address) > 2:
                addresses.append(address)
            address = ""
        address += c
        if c.isalpha():
            prevChar = True
        else:
            prevChar = False

    return address




file = open('AA315NYNORTHHEMP.PDF', 'rb')

fileReader = PyPDF2.PdfFileReader(file)
pageNum = fileReader.numPages
total_address = []
for i in range(0, pageNum - 1):
    page = fileReader.getPage(i)
    text = page.extractText()
    addresses = parsePageText(text)
    if (len(addresses) > 1) :
        total_address.append(addresses)

list = pd.Series(total_address)

list.to_csv("output.csv", index=False)
