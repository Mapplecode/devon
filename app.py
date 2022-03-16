from flask import Flask
from flask import render_template,request,jsonify,json
from categories import start_scrap
import pandas as pd
import os
from filecompair import file_compair

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/compair")
def compair():
    scrap_folder_files = os.listdir('scraps')
    print(scrap_folder_files)
    return render_template('compair.html',scrap_folder_files=scrap_folder_files)


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
    except Exception as e :
        print(e)
        return jsonify({'message':str(e)})


@app.route('/start_scrap')
def start_scrap():
    start_scrap()






if __name__ == "__main__":
   app.run(debug=True, use_debugger=False, use_reloader=False)
