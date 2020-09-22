from flask import Flask
from filesbuilder import FilesBuilder
from inputoutput import IO


class Bootstrap:

    def __init__(self, request, response):
        self.request = request
        self.response = response
        self.response['logs_messages'].append('File builder initiated...\n')
        self.file_builder = FilesBuilder(request)
        self.io_object = IO(self.request)
        self.response['logs_messages'].append('Old files cleaned\n')
        self.io_object.cleanUpOldData()
        self.io_object.createFolders()

    def getPath(self, subfolder=False):
        return self.io_object.getFolderPath(subfolder)

    def run(self, path):
        if 'text' in self.request['file_type']:
            self.response['logs_messages'].append('Building text file...\n')
            size = 1000000
            if 'KB' in self.request['file_size']:
                size=500
            file_name, content = self.file_builder.buildTextFile(length=size)
            try:
                self.io_object.writeTextFile(file_name=file_name, path=path, content=content)
                self.response['logs_messages'].append('Success!: Text file created\n')
            except:
                self.response['logs_messages'].append('Error: while writing text file\n')

        if 'pdf' in self.request['file_type']:
            self.response['logs_messages'].append('Building text file...\n')
            size = 1000000
            if 'KB' in self.request['file_size']:
                size=500
            file_name, content = self.file_builder.buildPdfFile(length=size)
            try:
                self.io_object.writePdfFile(file_name=file_name, path=path, content=content)
                self.response['logs_messages'].append('Success!: PDF file created\n')
            except:
                self.response['logs_messages'].append('Error: while writing pdf file\n')

        if 'xlsx' in self.request['file_type']:
            self.response['logs_messages'].append('Building text file...\n')
            size = 1000000
            if 'KB' in self.request['file_size']:
                size=500
            file_name, content = self.file_builder.buildXlsFile(length=size)
            try:
                self.io_object.writeExcelFile(file_name=file_name, path=path, content=content)
                self.response['logs_messages'].append('Success!: PDF file created\n')
            except:
                self.response['logs_messages'].append('Error: while writing pdf file\n')


        if 'image' in self.request['file_type']:
            self.response['logs_messages'].append('Building image files ..\n')
            width = 1920
            height = 1080
            if 'KB' in self.request['file_size']:
                width=400
                height=400

            png_file_name, jpg_file_name = self.file_builder.buildImageFile()
            try:
                self.io_object.writeImageFile(file_name=png_file_name, width=width, height=height, path=path)
                self.response['logs_messages'].append('Success!: PNG file created.\n')
            except:
                self.response['logs_messages'].append('Error: while creating PNG\n')

            try:
                self.io_object.writeImageFile(file_name=jpg_file_name, width=width, height=height, path=path)
                self.response['logs_messages'].append('Success! JPG file created\n')
            except:
                self.response['logs_messages'].append('Error: while creating JPG\n')

#writeExcelFile


if __name__ == '__main__':
    App = Bootstrap()
    App.run()