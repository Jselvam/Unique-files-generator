class Request:

    def __init__(self, resobj):
        self.req = {
            'error': False,
            'message': '',
            'foldername':'',
            'file_size':[],
            'file_type':[]
        }
        self.response = resobj
        self.response['logs_messages'].append('Processing request...\n')

    def processRequest(self, request):
        sub_folder = request.form["foldername"].strip()
        self.req['file_size'] = request.form.getlist('size')
        self.req['file_type'] = request.form.getlist('filetype')
        if sub_folder:
            self.response['logs_messages'].append('Validating user input...\n')
            self.req['foldername'] = sub_folder
        return self.req


