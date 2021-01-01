from flask import Flask
from flask_cors import CORS
from flask import send_file
import os

app = Flask(__name__)
CORS(app)

directory = "/home/images/"

@app.route("/", methods=['GET'])
def get_directory_list():
    elements = ""
    for el in os.listdir(directory):
        elements = elements + el + "\n"
    return elements

@app.route("/<index>", methods=['GET'])
def get_frame(index):
    return send_file(directory+"frame"+index+".jpg", mimetype='image/jpg')



if __name__ == '__main__':
    #collect_th = threading.Thread(target=collect_thread)
    #collect_th.start()
    app.run(port=3000)
