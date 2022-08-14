import datetime
from flask import Flask, request, jsonify
import dataframe
import db
import EDA

app = Flask(__name__)


@app.route('/')
def index():
    return "INVEZTO"


ALLOWED_EXTENSIONS = set(['csv', 'xls', 'xlsx'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_data():
    if 'file' not in request.files:
        return jsonify('No Data found')
    file = request.files['file']
    name = file.filename
    if file.filename == '':
        return jsonify('No Data found')
    if file and allowed_file(file.filename):
        df = dataframe.get_data(file, name)
        db.set_data(name, df)
        print(df)
        return jsonify(name=name, message='Data Uploaded Successfully!')
    else:
        return jsonify('Allowed types are - csv, xls, xlsx')


@app.route('/opening_clossing_trends', methods=['POST'])
def get_graph_1():
    name = request.form['name']
    return jsonify(EDA.opening_closing_trends_graph(name))


if __name__ == '__main__':
    app.run(debug=True)
