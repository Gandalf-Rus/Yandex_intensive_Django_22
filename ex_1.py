import sys

list_of_rows = []
dict_of_S = {}
for line in sys.stdin:
    list_of_rows.append(line.strip().upper())
max_max_S = 0

for row in list_of_rows:
    max_cnt_S = 0
    cnt_S = 0

    for i in range(len(row)):
        if row[i] == "S":
            cnt_S = cnt_S + 1
        else:
            if max_cnt_S < cnt_S:
                max_cnt_S = cnt_S
            cnt_S = 0
    if cnt_S > 0:
        if max_cnt_S < cnt_S:
            max_cnt_S = cnt_S
        cnt_S = 0
    if max_cnt_S > max_max_S:
        max_max_S = max_cnt_S
    if max_cnt_S > 0:
        dict_of_S[row] = max_cnt_S

max_list_S = []

for string in dict_of_S.keys():
    if dict_of_S[string] == max_max_S:
        max_list_S.append(string)

if max_list_S != []:
    longest_len = max([len(string) for string in max_list_S])
    longest_strings = []

    for string in max_list_S:
        if len(string) == longest_len:
            longest_strings.append(string)
            break
    longest_strings.sort()
    substrings = longest_strings[0].split("S")

    longest_len_sub = max([len(string) for string in substrings])
    for string in substrings:
        if len(string) == longest_len_sub:
            print(string)
            break
