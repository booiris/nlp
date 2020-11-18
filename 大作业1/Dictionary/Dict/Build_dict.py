import re

dic = {}
pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）|——|《|》|：|\n|\r|．|”|“|『|』|[１-９]'
with open("train_dict.txt", "r", encoding='utf-8') as f:
    for line in f:
        now_str = re.split(pattern, line)  # 处理标点和数字
        for word in now_str:
            if word == '' or word.isdigit():
                continue
            if word not in dic:
                dic[word] = 0
            dic[word] += 1

with open("dict.txt", "w", encoding='utf-8') as f:
    for key in dic:
        now_str = key + " " + str(dic[key]) + "\n"
        f.writelines(now_str)
