from csv_diff import load_csv, compare
import os
import pprint
import csv
COMPAIR_FILE_NAME = os.path.join(os.getcwd(),'difference_checker.csv')
from datetime import datetime


def file_compair(file_1,file_2):
    try:
        os.remove(COMPAIR_FILE_NAME)
    except:
        pass
    print(file_1,file_2)
    CSV_1 = load_csv(open(file_1), key="id")
    CSV_2 = load_csv(open(file_2), key="id")
    diff = compare(CSV_1,CSV_2)
    detailList = list()
    detailList.append(['id', 'name', 'price', 'size', 'availablity','action'])
    tr_string = ''
    for action in diff.keys():
        inner_data = diff[action]
        for ind in inner_data:
            try:
                if 'key' not in ind.keys():
                    print(inner_data,'no-key')
                    id = str(ind['id'])
                    name = str(ind['name'])
                    size = str(ind['size'])
                    price = str(ind['price'])
                    availablity = str(ind['availablity'])
                else:
                    print(inner_data)
                    id = str(ind['key'])
                    name = ' -- '
                    size =  '  --  '
                    availablity = '  --  '
                    price = '  --  '
                    change = ind['changes']
                    if 'availablity' in change.keys():
                        availablity = change['availablity'][1]
                    if 'name' in change.keys():
                        name = ind['changes']['name'][1]
                    if 'size' in change.keys():
                        size = ind['changes']['size'][1]
                    if 'price' in change.keys():
                        price = ind['changes']['price'][1]
                detailList.append([id,name, price, size, availablity,str(action).capitalize()])
                new_tr = ''
                new_tr =  "<tr class='"+str(action)+" actions'>"+"<td>"+str(id)+"</td>" + "<td>"+str(name)+"</td>" + "<td>"+str(price)+"</td>"+ "<td>"+str(size)+"</td>"+ "<td>"+str(availablity).capitalize()+"</td>" +   "<td>"+str(action).capitalize()+"</td>" +  "</tr>"
                tr_string = tr_string + new_tr
            except Exception as e:
                print(e)
    filename = 'compair.csv'
    write_csv(detailList, filename=filename)
    print(tr_string)
    return tr_string

def write_csv(rows,filename):
    # fields = ['Product Name', 'Price', 'Size', 'Status']
    rows = rows
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    print("[INFO] File write successfull.")

def get_scrap_data_files():
    scraps_path = os.path.join(os.getcwd(), 'scraps')
    if not os.path.exists(scraps_path):
        os.mkdir(scraps_path)
    scrap_folder_files = os.listdir('scraps')
    print(scrap_folder_files)
    new_tr = ''
    for file in scrap_folder_files:
        full_file_path = os.path.join(scraps_path,file)
        print(os.path.exists(full_file_path))
        time_is = os.path.getmtime(full_file_path)
        mod_time = datetime.fromtimestamp(time_is)
        print(mod_time)

        new_tr += "<tr class='""'>" + \
                 "<td>" + str(file) + "</td>" +\
                 "<td>" + str(mod_time) + "</td>" + \
                 "<td > <button type='button' " \
                 " class='btn btn-danger action_btn'>Delete</button> </td>" +  \
                 "</tr>"
    return new_tr

def delete_scrap_file_path(file_name):
    scraps_path = os.path.join(os.getcwd(), 'scraps')
    if not os.path.exists(scraps_path):
        os.mkdir(scraps_path)
    os.remove(os.path.join(scraps_path,file_name))
    return 'Delete Sucessfull'