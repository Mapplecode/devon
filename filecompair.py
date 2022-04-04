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
    CSV_1 = load_csv(open(file_1), key="id")
    CSV_2 = load_csv(open(file_2), key="id")
    diff = compare(CSV_1,CSV_2)
    tr_string = ''
    for action in diff.keys():
        inner_data = diff[action]
        for ind in inner_data:
            for id in CSV_1:
                try:
                    print(id)
                    if str(CSV_1[id]) != 'None' and str(CSV_2[id]) != 'None' and str(id) != 'None':
                        if CSV_1[id]['name'] != CSV_2[id]['name'] or CSV_1[id]['price'] != CSV_2[id]['price'] or \
                                CSV_1[id]['size'] != CSV_2[id]['size'] or CSV_1[id]['availablity'] != CSV_2[id][
                            'availablity']:

                            print('SAME')
                        else:
                            print(id)
                            print(CSV_1[id]['price'], '---', CSV_2[id]['price'])

                except:
                    print('NEW DATA')
            try:
                id = str(ind['id'])
                name = str(ind['name'])
                size = str(ind['size'])
                price = str(ind['price'])
                new_tr = ''
                new_tr =  "<tr class='"+str(action)+" actions'>"+"<td>"+str(id)+"</td>" + "<td>"+str(name)+"</td>" + "<td>"+str(price)+"</td>"+ "<td>"+str(size)+"</td>"+ "<td>"+str(action).capitalize()+"</td>" +  "</tr>"
                tr_string = tr_string + new_tr
                try:
                    write_compair([id,name,size,price,str(action).capitalize()])
                except Exception as e:
                    print('DIFF NOT WRITEN TO CSV')
                    print(e)

            except Exception as e:
                print(e)

    return tr_string

def write_compair(row):
    with open(COMPAIR_FILE_NAME, 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(row)