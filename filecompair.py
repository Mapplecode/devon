from csv_diff import load_csv, compare
import os
import pprint
import csv
COMPAIR_FILE_NAME = os.path.join(os.getcwd(),'difference_checker.csv')

def file_compair(file_1,file_2):
    try:
        os.remove(COMPAIR_FILE_NAME)
    except:
        pass
    print(file_1,file_2)
    CSV_1 = load_csv(open(file_1), key="id")
    CSV_2 = load_csv(open(file_2), key="id")
    diff = compare(CSV_1,CSV_2)
    tr_string = ''
    for action in diff.keys():
        inner_data = diff[action]
        for ind in inner_data:
            try:
                if inner_data != 'changed':
                    id = str(ind['id'])
                    name = str(ind['name'])
                    size = str(ind['size'])
                    price = str(ind['price'])
                    availablity = str(ind['availablity'])
                else:
                    id = str(ind['key'])
                    name = ''
                    size =  ''
                    availablity = ''
                    change = ind['changed']['changes']
                    if change == 'availablity':
                        availablity = ind['changed']['changes'][1]
                    if change == 'name':
                        name = ind['changed']['changes'][1]
                    if change == 'size':
                        size = ind['changed']['changes'][1]
                    if change == 'price':
                        price = ind['changed']['changes'][1]
                new_tr = ''
                new_tr =  "<tr class='"+str(action)+" actions'>"+"<td>"+str(id)+"</td>" + "<td>"+str(name)+"</td>" + "<td>"+str(price)+"</td>"+ "<td>"+str(size)+"</td>"+ "<td>"+str(availablity).capitalize()+"</td>" +   "<td>"+str(action).capitalize()+"</td>" +  "</tr>"
                tr_string = tr_string + new_tr
            except Exception as e:
                print(e)
    print(tr_string)
    return tr_string

