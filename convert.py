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
from PIL import Image
import zipfile
import win32com.client
from tempfile import mktemp
from threading import Thread

class Mixin(object):

    def __init__(self, files):
        """

        state 状态码：
        0 未启动
        1 测试
        2 转换为pdf
        3 盖章
        4 合并
        """
        self.files = files
        self.err = None
        self.errcode = 0
        self.prgbar_max = 0
        self.prgbar_val = 0
        self.state = 0
        self.doc = []
        self.xls = []
        self.pdf = []
        self.outfile = None

class Checker(Mixin):

    def check(self):
        """检测并提示错误
            err为3 pdf检测错误
            err为2 xls检测错误
            err为1 doc检测错误

            如果合法的话，就按照分类分好
        """
        self.state = 1
        self.prgbar_max = len(self.files.keys())
        self.prgbar_val = 0
        for item in self.files.keys():
            self.prgbar_val += 1
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
        """word转为pdf

           先尝试使用office word来做转换，
           再使用wps来做转换。

           office软件转换文档为pdf时，会自动加上pdf结尾，
           所以返回的临时文件要加上pdf的后缀。
        """
        tempfile = mktemp()
        wdFormatPDF = 17
        use_wps = False
        state = False
        try:
            word = win32com.client.Dispatch('Word.Application')
            doc = word.Documents.Open(filename)
            doc.SaveAs(tempfile, FileFormat=wdFormatPDF)
            doc.Close()
            state = True
        except Exception as e:
            self.err = str(e)
            use_wps = True
        finally:
            try:
                word.Quit()
            except Exception as e:
                self.err = str(e)

        # wps转换
        if use_wps:
            try:
                wps = win32com.client.Dispatch("KWPS.Application")
                doc = wps.Documents.Open(filename)
                doc.SaveAs(tempfile, wdFormatPDF)
                doc.Close()
                state = True
            except Exception as e:
                self.err = str(e)
                self.errcode = 10
            finally:
                try:
                    wps.Quit()
                except Exception:
                    self.errcode = 110

        if state:
            return "{}.pdf".format(tempfile)
        else:
            return False

    def xlsToPdf(self, filename):
        """execl转为pdf

            先使用excel来做转换，再使用et来做转换
        """
        tempfile = mktemp()
        xlFormatPDF = 57
        use_et = False  # 是否使用et
        state = False  # 转换状态
        # excel = comtypes.client.CreateObject('Excel.Application')
        try:
            excel = win32com.client.Dispatch('Excel.Application')
            wb = excel.Workbooks.Open(filename)
            wb.SaveAs(tempfile, FileFormat=xlFormatPDF)
            wb.Close()
            state = True
        except Exception as e:
            self.err = str(e)
            use_et = True
        finally:
            try:
                excel.Quit()
            except Exception as e:
                self.err = str(e)
        # et转换
        if use_et:
            try:
                et = win32com.client.Dispatch('KET.Application.9')
                workbook = et.Workbooks.Open(filename)
                workbook.ExportAsFixedFormat(0, tempfile)
                workbook.Close()
                state = True
            except Exception as e:
                self.err = str(e)
                self.errcode = 11
            finally:
                try:
                    et.Quit()
                except Exception:
                    self.errcode = 111

        if state:
            return "{}.pdf".format(tempfile)
        else:
            return False

    def convert(self):
        """转换为pdf
        """
        self.state = 2
        self.prgbar_max = len(self.doc) + len(self.xls)
        self.prgbar_val = 0
        for item in self.doc:
            self.prgbar_val += 1
            filepath = self.files[item][0]
            trans = self.docToPdf(filepath)
            if trans is not None:
                self.files[item][0] = trans
            else:
                return 2
        for item in self.xls:
            self.prgbar_val += 1
            filepath = self.files[item][0]
            trans = self.xlsToPdf(filepath)
            if trans is not None:
                self.files[item][0] = trans
            else:
                return 2

        return 0

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
        # 渲染图片
        img = self.transparent(item[1])
        # 新建一个新的pdf
        c = canvas.Canvas(tempmark)
        c.drawImage(img, width * rate, height * rate, mask='auto')
        c.save()
        # 打开pdf
        watermark = PdfFileReader(open(tempmark, 'rb'))
        outfile = PdfFileWriter()

        pagecount = infile.getNumPages()

        # 为每一页添加水印
        for page_num in range(pagecount):
            self.prgbar_val += 1
            inpage = infile.getPage(page_num)
            inpage.mergePage(watermark.getPage(0))
            outfile.addPage(inpage)

        # 输出到输出文件
        with open(tempout, 'wb') as outpdf:
            outfile.write(outpdf)

        return tempout

    def setMark(self):
        self.state = 3
        self.prgbar_max = 0
        self.prgbar_val = 0
        # 计算总页数
        for item in [*self.doc, *self.xls, *self.pdf]:
            if isinstance(self.files[item][1], str):
                src = self.files[item][0]
                pdfreader = PdfFileReader(open(src, 'rb'))
                self.prgbar_max += pdfreader.getNumPages()
        # 操作
        for item in [*self.doc, *self.xls, *self.pdf]:
            if isinstance(self.files[item][1], str):
                self.files[item][0] = self.mark(item)

    def transparent(self, image):
        """透明化处理"""
        handle_file = mktemp() + '.png'
        img = Image.open(image)
        # 全部设为0.75透明
        img.putalpha(192)
        # 处理全部白色为全透明
        img = img.convert("RGBA")
        data = img.getdata()

        new_data = []
        for ele in data:
            if ele[0] == 255 and ele[1] == 255\
                    and ele[2] == 255:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(ele)
        img.putdata(new_data)
        img.save(handle_file, "PNG")

        return handle_file

class FullConverter(Checker, Converter, WaterMark):

    def concat(self):
        """将多个pdf文件合成一个"""
        self.prgbar_max = 0
        self.prgbar_val = 0
        tempout = mktemp()
        outfile = PdfFileWriter()
        # 计算总页数
        for item in [*self.doc, *self.xls, *self.pdf]:
            src = self.files[item][0]
            pdfreader = PdfFileReader(open(src, 'rb'))
            self.prgbar_max += pdfreader.getNumPages()
        for item in self.files.values():
            infile = PdfFileReader(open(item[0], 'rb'))
            pagecount = infile.getNumPages()
            for page_num in range(pagecount):
                self.prgbar_val += 1
                inpage = infile.getPage(page_num)
                outfile.addPage(inpage)

        with open(tempout, 'wb') as pdfout:
            outfile.write(pdfout)

        return tempout

    def execute(self):
        """执行流程与check处理
        """
        self.check()
        if self.errcode != 0:
            return 1
        else:
            if self.errcode == 0:
                self.convert()
            if self.errcode == 0:
                self.setMark()
            if self.errcode == 0:
                self.outfile = self.concat()

    def run_thread(self):
        """多线程方式运行
        """
        t = Thread(target=self.execute, args=())
        t.start()
