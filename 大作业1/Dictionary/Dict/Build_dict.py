import re

dic = {}
with open("../../File/train_dict.txt", "r", encoding='utf-8') as f:
    # 构建字典
    for line in f:
        line = line.split()
        for word in line:
            now_str = ""
            for char in word:
                if '\u4e00' <= char <= '\u9fa5':
                    now_str += char
            if now_str:
                if now_str not in dic:
                    dic[now_str] = 0
                dic[now_str] += 1


with open("dict.txt", "w", encoding='utf-8') as f:
    for key in dic:
        now_str = key + " " + str(dic[key]) + "\n"
        f.writelines(now_str)
