import PyPDF2

# パスリストを取得する
def getPassList():
    f = open('./password/passwordList.txt')
    lines = f.readlines()
    passList = []
    for line in lines:
        passList.append(line.replace('\n',''))
    return passList


# パスワード付与
def grantPass(passList) :
    src_pdf = PyPDF2.PdfFileReader('import/test.pdf',strict=False)
    dst_pdf = PyPDF2.PdfFileWriter()

    dst_pdf.cloneReaderDocumentRoot(src_pdf)
    print('ここまできた')

    dst_pdf.encrypt('1234')
    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}
    dst_pdf.addMetadata(d)
    with open('output/test.pdf', 'wb') as pdfFileObj2:
        dst_pdf.write(pdfFileObj2)




# メインメソッド
print('スタート')

# パスリストを取得する。
passList = getPassList()

for passWord in passList :
    print(passWord)

grantPass(passList)