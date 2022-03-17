from csv_diff import load_csv, compare
import os
import pprint


# def test():
#     fileone = "/home/mapple/PycharmProjects/devon/scraps/2022-03-07 13:10:25.311873_.csv"
#     filetwo = "/home/mapple/PycharmProjects/devon/scraps/2022-03-15 13:07:02.419459_.csv"
#
#     path = os.path.join(os.getcwd(),'scraps')
#     diff = compare(
#         load_csv(open(fileone), key="id"),
#         load_csv(open(filetwo), key="id")
#     )
#     # pprint.pprint(diff.keys())
#     changed_data = diff['changed']
#     added_data = diff['added']
#     removed_data = diff['removed']
#     print(removed_data)
#     tr_string = ''
#     for action in diff.keys():
#         print(action)
#
#     with open(fileone, 'r') as file1:
#         with open(filetwo, 'r') as file2:
#             difference = set(file1).difference(file2)
#
#     difference.discard('\n')
#
#     with open(path+'/'+'diff.txt', 'w') as file_out:
#         for line in difference:
#             file_out.write(line)

def file_compair(file_1,file_2):
    diff = compare(
        load_csv(open(file_1), key="id"),
        load_csv(open(file_2), key="id")
    )
    tr_string = ''
    for action in diff.keys():
        inner_data = diff[action]
        for ind in inner_data:
            try:
                id = str(ind['id'])
                name = str(ind['name'])
                size = str(ind['size'])
                price = str(ind['price'])
                new_tr = ''
                new_tr =  "<tr class='"+str(action)+" actions'>"+"<td>"+str(id)+"</td>" + "<td>"+str(name)+"</td>" + "<td>"+str(price)+"</td>"+ "<td>"+str(size)+"</td>"+ "<td>"+str(action).capitalize()+"</td>" +  "</tr>"
                tr_string = tr_string + new_tr
            except Exception as e:
                print(e)
    print(tr_string)
    return tr_string
