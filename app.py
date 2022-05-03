from flask import Flask
from flask import render_template,request,jsonify,json,send_file
from categories import start_scrap
import pandas as pd
import os
import csv
from filecompair import file_compair,get_scrap_data_files,delete_scrap_file_path
import os
from flask import send_file,make_response,Response,send_file


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/compair")
def compair():
    scraps_path = os.path.join(os.getcwd(),'scraps')
    if not os.path.exists(scraps_path):
        os.mkdir(scraps_path)
    scrap_folder_files = os.listdir('scraps')
    print(scrap_folder_files)
    return render_template('compair.html',scrap_folder_files=scrap_folder_files)



@app.route("/get_scrap_files",methods=['POST','GET'])
def get_scrap_files():
    data = ''
    data = get_scrap_data_files()
    print(data)
    return jsonify({'data_list':data})


@app.route("/delete_scrap_files",methods=['POST','GET'])
def delete_scrap_file():
    param = {}
    if request.method == 'GET':
        param = request.args
    elif request.method == 'POST':
        param = request.form
    file_name = param.get('file_name')
    data = ''
    data = delete_scrap_file_path(file_name)
    return jsonify({'data':data})

@app.route("/download_scrap")
def download_scrap():
    data = get_scrap_data_files()
    print(data)
    return render_template('download_scrap.html',data_list = data)

@app.route('/compair_files',methods=['POST','GET'])
def compair_files():
    param = {}
    data = {}
    try:
        if request.method == 'GET':
            param = request.args
        elif request.method == 'POST':
            param = request.form
        path = os.path.join(os.getcwd(),'scraps')
        file1 = os.path.join(path,param.get('file1') )
        file2 = os.path.join(path, param.get('file2') )
        data = file_compair(file1,file2)
        print(data)
        return jsonify({'data':data})
    except Exception as e:
        print(e)
        return jsonify({'message':str(e)})


@app.route('/start_scrap')
def start_scrap1():
    start_scrap()

@app.route("/scraping")
def scraping():
    try:
        os.remove("count_file.txt")
    except:
        pass
    return render_template('scraping.html')

@app.route("/remaining_products")
def remaining_products():
    if os.path.exists('count_file.txt'):
        read_file = 'count_file.txt'
        str1 = open(read_file,'r').read()
        return {'data': 'Remaining products - '+str(str1)}
    else:
        return {'data':''}


@app.route('/download_file') # this is a job for GET, not POST
def plot_csv():
    return send_file('compair.csv',
                     mimetype='text/csv',
                     attachment_filename='compair.csv',
                     as_attachment=True)
@app.route('/download_scrap',methods=['POST','GET'])
def plot_csv2():
    param = {}
    data = {}
    try:
        if request.method == 'GET':
            param = request.args
        elif request.method == 'POST':
            param = request.form
    except:
        pass
    file = param.get('file')
    return send_file(file,
                     mimetype='application/vnd.ms-excel',
                     attachment_filename=file,
                     as_attachment=True)
# if __name__ == "__main__":
#    app.run(debug=True, use_debugger=False, use_reloader=False)

