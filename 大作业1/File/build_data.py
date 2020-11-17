# res = ""
# with open("data.txt", "r", encoding='utf-8') as f:
#     for line in f:
#         word = line.split()
#         for i in range(len(word)):
#             if i == 0:
#                 continue
#             char = word[i]
#             char = char.split("/")
#             res += char[0]
#         res += '\n'
# print(len(res))
# with open("test_data.txt", "w+",encoding='utf-8') as f:
#     f.writelines(res)


with open("data.txt", "r", encoding='utf-8') as f:
    f1 = open("real_data.txt", "w+", encoding='utf-8')
    for line in f:
        word = line.split()
        res = ""
        for i in range(len(word)):
            if i == 0:
                continue
            res += word[i]+' '
        res += '\n'
        f1.writelines(res)
    f1.close()
