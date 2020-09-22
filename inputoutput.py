import os
import shutil
import platform
import time
import numpy
from PIL import Image, ImageFilter
from fpdf import FPDF
from xlwt import Workbook

class IO(object):
    """All input output operation (Files Read, Write ) done in this class """

    def __init__(self, request):
        self.request = request
        self.logger = os.getcwd() + '/logs/'
        self.utility = Utility()
        self.data_folder = self.utility.getDesktopLocation() + '/qatest_DATA-9921/'
        self.sub_folder = 'subfolder_test'

    def getFolderPath(self, subfolder=False):
        if subfolder:
            return self.sub_folder+'/'
        return self.data_folder

    def cleanUpOldData(self):
        self.data_folder = self.utility.getDesktopLocation() + '/qatest_DATA-9921/'
        if os.path.exists(self.data_folder):
            shutil.rmtree(self.data_folder)

    def createFolders(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
            if self.request['foldername']:
                self.sub_folder = self.data_folder + self.request['foldername']
            else:
                self.sub_folder = self.data_folder + self.sub_folder

            if not os.path.exists(self.sub_folder):
                os.makedirs(self.sub_folder)

    def writeTextFile(self, file_name=None,
                      path=None,
                      content=None):
        try:
            file = open(path + file_name, "w+")
            file.write(content)
        except:
            print(f"Error writing the file {path + file_name}")
        finally:
            file.close()

    def writeImageFile(self, file_name=None,
                       path=None,
                       width=1920,
                       height=1080,
                       num_of_images=1):


        try:
            width = int(width)
            height = int(height)
            num_of_images = int(num_of_images)
            for n in range(num_of_images):
                filename = path + file_name
                rgb_array = numpy.random.rand(height, width, 3) * 255
                image = Image.fromarray(rgb_array.astype('uint8')).filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3)).convert('RGB')
                image.save(filename, quality=10)
        except:
            print(f"Error writing the Image file {path + file_name}")

    def writePdfFile(self, file_name=None,
                      path=None,
                      content=None):
        i = 1
        try:
            filename = path + file_name
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=15)
            for line_num in range(0, len(content), 50):
                eachline = content[line_num:line_num + 50]
                pdf.cell(200, 10, txt=eachline,
                         ln=i, align='C')
                i += 1

            pdf.output(filename)
        except:
            print(f"Error writing the PDF file {path + file_name}")

    def writeExcelFile(self, file_name=None,
                      path=None,
                      content=None):
        i = 1
        try:
            filename = path + file_name
            wb = Workbook()
            # add_sheet is used to create sheet.
            sheet1 = wb.add_sheet('Sheet 1')
            for line_num in range(0, len(content), 50):
                eachline = content[line_num:line_num + 50]
                sheet1.write(i, 0, eachline)
                i += 1

            wb.save(filename)
        except:
            print(f"Error writing the Excel file {path + file_name}")

class Utility:

    def getOSType(self):
        operating_system = platform.system()
        return operating_system

    def getDesktopLocation(self):
        user_os = self.getOSType()
        desktop = ''
        if user_os == 'Windows':
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        else:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        return desktop


if __name__ == '__main__':
    help(Image)

