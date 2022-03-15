from csv_diff import load_csv, compare
import os
import pprint
path = os.path.join(os.getcwd(),'scraps')
diff = compare(
    load_csv(open(path+'/'+"2022-03-07 13:10:25.311873_.csv"), key="id"),
    load_csv(open(path+'/'+"2022-03-14 13:36:10.284265_.csv"), key="id")
)
pprint.pprint(diff)

fileone = path+'/'+"2022-03-07 13:10:25.311873_.csv"
filetwo = path+'/'+"2022-03-14 13:36:10.284265_.csv"

# with open(fileone, 'r') as file1:
#     with open(filetwo, 'r') as file2:
#         same = set(file1).intersection(file2)

# same.discard('\n')

# with open('some_output_file.txt', 'w') as file_out:
#     for line in same:
#         file_out.write(line)


with open(fileone, 'r') as file1:
    with open(filetwo, 'r') as file2:
        difference = set(file1).difference(file2)

difference.discard('\n')

with open(path+'/'+'diff.txt', 'w') as file_out:
    for line in difference:
        file_out.write(line)
