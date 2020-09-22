from flask import Flask, render_template, request
from Response import Response
from Request import Request
from bootstrap import Bootstrap
from webui import WebUI
import json


app = Flask(__name__)
ui = WebUI(app, debug=True) # Create a WebUI instance
res = Response()
gresponse = res.homepageResponse()

@app.route("/", methods=["POST", "GET"])
def homepage():
    global gresponse
    reqObj = Request(gresponse)
    if request.method == "POST":
        datahopper = reqObj.processRequest(request)
        generator = Bootstrap(datahopper, gresponse)
        path = generator.getPath(subfolder=False)
        generator.run(path)
        gresponse['logs_messages'].append('Write subfolder in progress!\n')
        path = generator.getPath(subfolder=True)
        generator.run(path)
        gresponse['logs_messages'].append('All the unique files created.\n')
        gresponse['ispost'] = 'true'
    gresponse['logs_messages'].append('Request served\n')
    return render_template("index.html",response=gresponse, jsdata=json.dumps(gresponse['logs_messages']))


if __name__ == "__main__":
    ui.run()