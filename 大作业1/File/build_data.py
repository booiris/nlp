# data生成real_data和test_data和speech_test_data      train_data生成train_dict和train_prob和ner_prob

# 生成test_data
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
#             if ']' in char[1]:
#                 res += ']'
#         res += '\n'
# print(len(res))
# with open("test_data.txt", "w+", encoding='utf-8') as f:
#     f.writelines(res)

# 生成speech_test_data
# res = ""
# with open("data.txt", "r", encoding='utf-8') as f:
#     for line in f:
#         word = line.split()
#         for i in range(len(word)):
#             if i == 0:
#                 continue
#             char = word[i]
#             char = char.split("/")
#             cnt = 0
#             for b in char[0]:
#                 if not '\u4e00' <= b <= '\u9fa5':
#                     res += b
#                     cnt += 1
#                 else:
#                     break
#             res += ' ' + char[0][cnt:] + ' '
#             if ']' in char[1]:
#                 res += '] '
#         res += '\n'
# with open("speech_test_data.txt", "w+", encoding='utf-8') as f:
#     f.writelines(res)

# 生成real_data
# with open("data.txt", "r", encoding='utf-8') as f:
#     f1 = open("real_data.txt", "w+", encoding='utf-8')
#     for line in f:
#         word = line.split()
#         res = ""
#         for i in range(len(word)):
#             if i == 0:
#                 continue
#             temp_str = ""
#             word_list = word[i].split("/")
#             if "]" in word_list[1]:
#                 temp_str += word_list[0] + '/'
#                 for char in word_list[1]:
#                     if char == ']':
#                         break
#                     temp_str += char
#                 temp_str += ' ' + ']' + "/m"
#                 word[i] = temp_str
#             res += word[i] + ' '
#         res += '\n'
#         f1.writelines(res)
#     f1.close()

# 生成train_dict
# with open("train_data.txt", "r", encoding='utf-8') as f:
#     f1 = open("train_dict.txt", "w+", encoding='utf-8')
#     for line in f:
#         word = line.split()
#         res = ""
#         for i in range(len(word)):
#             if i == 0:
#                 continue
#             temp = word[i].split("/")
#             res += temp[0] + ' '
#         res += '\n'
#         f1.writelines(res)
#     f1.close()

# 生成train_prob
# with open("train_data.txt", "r", encoding='utf-8') as f:
#     f1 = open("train_prob.txt", "w+", encoding='utf-8')
#     for line in f:
#         word = line.split()
#         res = ""
#         for i in range(len(word)):
#             if i == 0:
#                 continue
#             temp_str = ""
#             word_list = word[i].split("/")
#             if "]" in word_list[1]:
#                 temp_str += word_list[0] + '/'
#                 for char in word_list[1]:
#                     if char == ']':
#                         break
#                     temp_str += char
#                 temp_str += ' ' + ']' + "/m"
#                 word[i] = temp_str
#             res += word[i] + ' '
#         res += '\n'
#         f1.writelines(res)
#     f1.close()

# 生成 ner_prob
with open("train_data.txt", "r", encoding='utf-8') as f:
    f1 = open("ner_prob.txt", "w+", encoding='utf-8')
    for line in f:
        word = line.split()
        res = ""
        for i in range(len(word)):
            if i == 0:
                continue
            word_list = word[i].split("/")
            if "]" in word_list:
                pass
