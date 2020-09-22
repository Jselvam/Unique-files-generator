from inputoutput import Utility


class Response:

    def __init__(self):
        self.utility = Utility()
        self.response = {
            'isError': False,
            'errorMessage': '',
            'response_message': '',
            'foldername': 'qatest_DATA-9921',
            'desktop_location': self.utility.getDesktopLocation(),
            'logs_messages':[],
            'ispost':'false'
        }

    def homepageResponse(self):
        return self.response
