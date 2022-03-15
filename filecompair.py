from csv_diff import load_csv, compare

diff = compare(
    load_csv(open("2022-03-07 13_10_25.311873_.csv"), key="id"),
    load_csv(open("2022-03-14 13_36_10.284265_.csv"), key="id")
)
print(diff)

fileone = "2022-03-07 13_10_25.311873_.csv"
filetwo = "2022-03-14 13_36_10.284265_.csv"

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

with open('diff.txt', 'w') as file_out:
    for line in difference:
        file_out.write(line)
