# data生成real_data和test_data和speech_test_data和real_ner_data
# real_data是测试集真实结果，test_data是测试集,speech_test_data是未标注词性的分词结果，用于词性标注
# train_data生成train_dict和train_prob和ner_prob
# tran_dict是用于训练词典分词的词典，train_prob用于训练统计分词的参数

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

# 生成real_ner_data
# with open("data.txt", "r", encoding='utf-8') as f:
#     save = []
#     f1 = open("real_ner_data.txt", "w+", encoding='utf-8')
#     for line in f:
#         save.clear()
#         now = '#'
#         word = line.split()
#         res = ""
#         for i in range(len(word)):
#             if i == 0:
#                 continue
#             temp_str = ""
#             word_list = word[i].split("/")
#             if word_list[1] == "nt":
#                 if now != "nt":
#                     for j in save:
#                         temp_str += j
#                     save.clear()
#                 save.append(word_list[0])
#             elif word_list[1] == "nr":
#                 if now != "nr":
#                     for j in save:
#                         temp_str += j
#                     save.clear()
#                 save.append(word_list[0])
#             elif word_list[1] == "ns":
#                 if now != "ns":
#                     for j in save:
#                         temp_str += j
#                     save.clear()
#                 save.append(word_list[0])
#             else:
#                 for j in save:
#                     temp_str += j
#                 save.clear()
#                 save.append(word_list[0])
#             if now == 'nr' or now == 'nt' or now == 'ns':
#                 if now == 'nr' and temp_str:
#                     if len(temp_str) == 1:
#                         res += temp_str[0] + '/S-PER '
#                     else:
#                         res += temp_str[0] + '/B-PER '
#                         for j in range(1, len(temp_str) - 1):
#                             res += temp_str[j] + '/I-PER '
#                         res += temp_str[len(temp_str) - 1] + 'E-PER '
#                 if now == 'nt' and temp_str:
#                     if len(temp_str) == 1:
#                         res += temp_str[0] + '/S-ORG '
#                     else:
#                         res += temp_str[0] + '/B-ORG '
#                         for j in range(1, len(temp_str) - 1):
#                             res += temp_str[j] + '/I-ORG '
#                         res += temp_str[len(temp_str) - 1] + 'E-ORG '
#                 if now == 'ns' and temp_str:
#                     if len(temp_str) == 1:
#                         res += temp_str[0] + '/S-LOC '
#                     else:
#                         res += temp_str[0] + '/B-LOC '
#                         for j in range(1, len(temp_str) - 1):
#                             res += temp_str[j] + '/I-LOC '
#                         res += temp_str[len(temp_str) - 1] + 'E-LOC '
#             else:
#                 for j in temp_str:
#                     res += j + '/o '
#
#             now = word_list[1]
#
#         temp_str = ""
#         for j in save:
#             temp_str += j
#         save.clear()
#         if now == 'nr' or now == 'nt' or now == 'ns':
#             if now == 'nr' and temp_str:
#                 if len(temp_str) == 1:
#                     res += temp_str[0] + '/S-PER '
#                 else:
#                     res += temp_str[0] + '/B-PER '
#                     for j in range(1, len(temp_str) - 1):
#                         res += temp_str[j] + '/I-PER '
#                     res += temp_str[len(temp_str) - 1] + 'E-PER '
#             if now == 'nt' and temp_str:
#                 if len(temp_str) == 1:
#                     res += temp_str[0] + '/S-ORG '
#                 else:
#                     res += temp_str[0] + '/B-ORG '
#                     for j in range(1, len(temp_str) - 1):
#                         res += temp_str[j] + '/I-ORG '
#                     res += temp_str[len(temp_str) - 1] + 'E-ORG '
#             if now == 'ns' and temp_str:
#                 if len(temp_str) == 1:
#                     res += temp_str[0] + '/S-LOC '
#                 else:
#                     res += temp_str[0] + '/B-LOC '
#                     for j in range(1, len(temp_str) - 1):
#                         res += temp_str[j] + '/I-LOC '
#                     res += temp_str[len(temp_str) - 1] + 'E-LOC '
#         else:
#             for j in temp_str:
#                 res += j + '/o '
#
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
# with open("train_data.txt", "r", encoding='utf-8') as f:
#     f1 = open("ner_prob.txt", "w+", encoding='utf-8')
#     for line in f:
#         flag = False
#         word = line.split()
#         res = ""
#         for i in range(len(word)):
#             if i == 0:
#                 continue
#             word_list = word[i].split("/")
#             if '[' in word_list[0]:
#                 res += word_list[0]
#                 flag = True
#                 continue
#             if ']' in word_list[1]:
#                 res += word_list[0] + ']' + '/nt '
#                 flag = False
#                 continue
#             if flag:
#                 res += word_list[0]
#                 continue
#             else:
#                 res += word[i] + ' '
#         f1.writelines(res + '\n')
