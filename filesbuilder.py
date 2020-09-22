from contentgenerator import ContentGenerator
class FilesBuilder:
    """ Create all type of file objects """

    def __init__(self, request):
        self.request = request
        self.content = ContentGenerator()
        self.file_types = {}
        self.text_line_length = 50

    def buildTextFile(self, length=10000):
        content = ''
        characters = self.content.getCharString(uppercase=False,
                                               specialChar=False,
                                               digits=False)

        text = self.content.getRandomString(length=length)
        for line_num in range(0, len(text), self.text_line_length):
            content += text[line_num:line_num + self.text_line_length] + "\n"

        file_name = 'TEXT-'+self.content.getRandomString(10,characters) + '.txt'

        return file_name, content

    def buildPdfFile(self, length=10000):
        content = ''
        characters = self.content.getCharString(uppercase=False,
                                               specialChar=False,
                                               digits=False)

        text = self.content.getRandomString(length=length)
        file_name = 'PDF-'+self.content.getRandomString(10,characters) + '.pdf'

        return file_name, text

    def buildXlsFile(self, length=10000):
        content = ''
        characters = self.content.getCharString(uppercase=False,
                                               specialChar=False,
                                               digits=False)

        text = self.content.getRandomString(length=length)
        file_name = 'Excel-'+self.content.getRandomString(10,characters) + '.xlsx'

        return file_name, text


    def buildImageFile(self):
        characters = self.content.getCharString(uppercase=False,
                                               specialChar=False,
                                               digits=False)
        # write png file
        png_file_name = 'IMAGE-PNG'+ self.content.getRandomString(10,characters) + '.png'
        # write jpg file
        jpg_file_name = 'IMAGE-JPG'+self.content.getRandomString(10,characters) + '.jpg'

        return png_file_name, jpg_file_name
