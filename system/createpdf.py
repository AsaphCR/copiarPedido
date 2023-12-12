import os
from system.utilities import *
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from barcode import EAN13
from barcode.writer import ImageWriter


class PDFDocument:
    def __init__(self, jsonObject, nomeDocumento) -> None:
        self.nomeDocumento = nomeDocumento
        self.__pdfConstruct(jsonObject)
    
    def __printerPDF(self, object, text) -> None:
        firstHifen = True
        minus = 11
        textSlice = ""
        object.setFont("Helvetica", 7.0)
        text = text.split(" ")
        for word in text:
            if word != "-":
                if len(textSlice) + len(word) < 30:
                    textSlice += word + " "
                else:
                    object.drawCentredString(self.xposition, self.yposition, textSlice)
                    self.yposition -= minus
                    textSlice = word + " "
            else:
                if firstHifen:
                    firstHifen = False
                    object.drawCentredString(self.xposition, self.yposition, textSlice)
                    self.yposition -= minus
                    textSlice = ""
                else:
                    textSlice += word + " "
        object.drawCentredString(self.xposition, self.yposition, textSlice)
        self.yposition -= minus
    
    def __codigoBarras(self, EAN) -> str:
        criarDiretorio("codigosdebarra")
        try:
            with open(os.path.abspath(f'codigosdebarra/{EAN}.jpg'), "rb") as _:
                ...
        except:
            with open(os.path.abspath(f'codigosdebarra/{EAN}.jpg'), "wb") as file:
                EAN13(str(EAN), writer=ImageWriter()).write(file, options={'font_size': 0})
        return os.path.abspath(f'codigosdebarra/{EAN}.jpg')

    def __pdfConstruct(self, jsonObject) -> None:
        width = 110.0 * mm
        height = 75.0 * mm
        pagesize = (width, height)
        criarDiretorio("Etiquetas")
        pdfdocument = canvas.Canvas(f"Etiquetas/{self.nomeDocumento}.pdf", pagesize=pagesize)
        pdfdocument.translate(mm, mm)
        mask = [50, 256, 50, 256, 50, 256]
        barcodedecrease = 18
        solitary_minus = 6
        count = 0
        for produto in jsonObject:
            repeticoes = produto['produto']['quantidade']
            aux = 0
            while aux < repeticoes:
                if count / 2 == 0:
                    barcodexposition = 1
                    logoxposition = 16
                    self.xposition = 76
                    self.yposition = 175
                else:
                    barcodexposition = 161
                    logoxposition = 176
                    self.xposition = 236
                    self.yposition = 175
                pdfdocument.drawImage(os.path.abspath("images/Logo_CarolRossato_Preto_menor.jpg"), logoxposition, self.yposition + 2, width=119, height=25, mask=mask)
                self.__printerPDF(pdfdocument, "Troca c/ etiqueta até 30 dias a partir de __/__/__")
                self.yposition -= 3
                self.__printerPDF(pdfdocument, produto['produto']['descricao'])
                self.yposition -= barcodedecrease
                pdfdocument.drawImage(self.__codigoBarras(produto['produto']['ean']), barcodexposition, self.yposition, width=150, height=25, mask=mask)
                self.yposition -= solitary_minus
                self.__printerPDF(pdfdocument, produto['produto']['ean'])
                self.yposition = 63
                self.__printerPDF(pdfdocument, produto['produto']['descricao'])
                self.__printerPDF(pdfdocument, f"R${produto['produto']['valor_unitario']:,.2f}".replace(",", "_").replace(".", ",").replace("_", "."))
                self.yposition -= barcodedecrease
                pdfdocument.drawImage(self.__codigoBarras(produto['produto']['ean']), barcodexposition, self.yposition, width=150, height=25, mask=mask)
                self.yposition -= solitary_minus
                self.__printerPDF(pdfdocument, produto['produto']['ean'])
                if count / 2 != 0:
                    pdfdocument.showPage()
                    count = 0
                else:
                    count += 1
                aux += 1
        pdfdocument.save()
