import PyPDF2
import os
import glob

# パスリストを取得する
def getPassList():
    f = open('./password/passwordList.txt')
    lines = f.readlines()
    passList = []
    for line in lines:
        passList.append(line.replace('\n',''))
    return passList

# サーチファイル
def serchFile(passList) :
    dirlist=[]
    # すべてのファイルを取得
    for name in glob.glob('import/*'):
        dirlist.append(name)
    # 該当するファイル名がパスリストを含んでる場合
    for passAndTitle in passList :
        title = passAndTitle.split("=")[0]
        password = passAndTitle.split("=")[1]
        for dirStr in dirlist :
            fileName = dirStr.split('/')[1] 
            if title in fileName :
                grantPass(fileName,password)

# パスワード付与
def grantPass(fileName,password) :
    src_pdf = PyPDF2.PdfFileReader('import/' + fileName ,strict=False)
    dst_pdf = PyPDF2.PdfFileWriter()

    dst_pdf.cloneReaderDocumentRoot(src_pdf)

    dst_pdf.encrypt(password)
    d = {key: src_pdf.documentInfo[key] for key in src_pdf.documentInfo.keys()}
    dst_pdf.addMetadata(d)
    with open('output/' + fileName, 'wb') as pdfFileObj2:
        dst_pdf.write(pdfFileObj2)


# メインメソッド
# パスリストを取得する。
passList = getPassList()

# パス付与
serchFile(passList)