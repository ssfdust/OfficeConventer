# -*- coding: utf-8 -*-
"""
南无大方广佛华严经，华严海会佛菩萨
南无大方广佛华严经，华严海会佛菩萨
南无大方广佛华严经，华严海会佛菩萨
南无大愿地藏王菩萨摩诃萨
南无大愿地藏王菩萨摩诃萨
南无大愿地藏王菩萨摩诃萨

转换模块

将docx, doc, xls, xlsx转换为pdf，且进行合并

"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.utils import PdfReadError
from reportlab.pdfgen import canvas
import zipfile
# import comtypes.client
from tempfile import mktemp

class Mixin(object):

    def __init__(self, files):
        """

        state 状态码：
        0 未启动
        1 测试
        2 转换为pdf
        3 盖章
        4 合并
        7 出错
        """
        self.files = files
        self.err = None
        self.errcode = 0
        self.state = 0
        self.doc = []
        self.xls = []
        self.pdf = []

class Checker(Mixin):

    def check(self):
        """检测并提示错误
            err为3 pdf检测错误
            err为2 xls检测错误
            err为1 doc检测错误

            如果合法的话，就按照分类分好
        """
        for item in self.files.keys():
            self.state = 1
            filepath = self.files[item][0]
            if filepath.endswith('.pdf'):
                if not self.isValidPdf(filepath):
                    self.errcode = 3
                    self.err = '{} 不合法'.format(filepath)
                    break
                else:
                    self.pdf.append(item)
            elif filepath.endswith('.xls') or filepath.endswith('.xlsx'):
                if not self.isValidXls(filepath):
                    self.errcode = 2
                    self.err = '{} 不合法'.format(filepath)
                    break
                else:
                    self.xls.append(item)
            elif filepath.endswith('.dox') or filepath.endswith('.docx'):
                if not self.isValidDoc(filepath):
                    self.errcode = 1
                    self.err = '{} 不合法'.format(filepath)
                    break
                else:
                    self.doc.append(item)

    def isdir(self, z, name):
        """检查是否为一个目录
        """
        return any(x.startswith("%s/" % name.rstrip("/")) for x in z.namelist())

    def isValidDoc(self, filename):
        """检查word文件是否合法
        """
        try:
            with zipfile.ZipFile(filename, 'r') as f:
                state = self.isdir(f, "word") and self.isdir(f, "docProps") and self.isdir(f, "_rels")

            return state
        except zipfile.BadZipfile:
            return False

    def isValidXls(self, filename):
        """检查excel文件是否合法
        """
        try:
            with zipfile.ZipFile(filename, 'r') as f:
                state = self.isdir(f, "xl") and self.isdir(f, "docProps") and self.isdir(f, "_rels")

            return state
        except zipfile.BadZipfile:
            return False

    def isValidPdf(self, filename):
        """检查pdf文件是否合法
        """
        with open(filename, 'rb') as f:
            try:
                PdfFileReader(f)
                state = True
            except PdfReadError:
                state = False

        return state

class Converter(Mixin):
    def docToPdf(self, filename):
        """word转为pdf"""
        tempfile = mktemp()
        wdFormatPDF = 17
        word = comtypes.client.CreateObject('Word.Application')
        doc = word.Documents.Open(filename)
        doc.SaveAs(tempfile, FileFormat=wdFormatPDF)
        doc.Close()
        word.Quit()

        return tempfile

    def xlsToPdf(self, filename):
        """execl转为pdf"""
        tempfile = mktemp()
        excel = comtypes.client.CreateObject('Excel.Application')
        wb = excel.Workbooks.Open(filename)
        ws = wb.Worksheets[1]
        wb.SaveAs(tempfile, FileFormat=57)
        wb.Close()
        excel.Quit()

        return tempfile

    def convert(self):
        """转换为pdf
        """
        self.state = 2
        for item in self.doc:
            filepath = self.files[item][0]
            trans = self.docToPdf(filepath)
            self.files[item][0] = trans
        for item in self.xls:
            filepath = self.files[item][0]
            trans = self.xlsToPdf(filepath)
            self.files[item][0] = trans

class WaterMark(Mixin):

    def mark(self, filename):
        """添加水印

            pdf添加水印只能通过新建一个pdf，在新建的
            文件中添加图片，然后保存。
            将新建的文件与水印文件，合并。一页一页地
            合并，完成后生成新文件即可。
            由于长宽不确定所以，计算了大概印章的位置，
            利用黄金分割比。

            返回输出文件
        """
        tempmark = mktemp()  # 水印文件
        tempout = mktemp()  # 输出文件
        item = self.files[filename]
        # 获取长宽
        infile = PdfFileReader(open(item[0], 'rb'))
        rate = 0.618
        mdbox = list(infile.getPage(0).mediaBox)
        # 按照黄金分割率放置图片
        width = float(mdbox[2] - mdbox[0])
        height = float(mdbox[3] - mdbox[1])
        # 新建一个新的pdf
        c = canvas.Canvas(tempmark)
        c.drawImage(item[1], width * rate, height * rate)
        c.save()
        # 打开pdf
        watermark = PdfFileReader(open(tempmark, 'rb'))
        outfile = PdfFileWriter()

        pagecount = infile.getNumPages()

        # 为每一页添加水印
        for page_num in range(pagecount):
            inpage = infile.getPage(page_num)
            inpage.mergePage(watermark.getPage(0))
            outfile.addPage(inpage)

        # 输出到输出文件
        with open(tempout, 'wb') as outpdf:
            outfile.write(outpdf)

        return tempout

    def setMark(self):
        self.state = 3
        for item in [*self.doc, *self.xls, *self.pdf]:
            if isinstance(self.files[item][1], str):
                self.files[item][0] = self.mark(item)

class FullConverter(Checker, Converter, WaterMark):

    def concat(self):
        """将多个pdf文件合成一个"""
        tempout = mktemp()
        outfile = PdfFileWriter()
        for item in self.files.values():
            infile = PdfFileReader(open(item[0], 'rb'))
            pagecount = infile.getNumPages()
            for page_num in range(pagecount):
                inpage = infile.getPage(page_num)
                outfile.addPage(inpage)

        with open(tempout, 'wb') as pdfout:
            outfile.write(pdfout)

        return tempout
