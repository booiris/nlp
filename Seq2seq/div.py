import jieba

jieba.enable_paddle()
jieba.set_dictionary('File/dict.txt.big')

f1 = open("File/train_data.txt", "w+", encoding='utf-8')

with open("File/data.txt", "r", encoding='utf-8') as f:
    for line in f:
        temp = line.split("\t")
        str_list = jieba.cut(temp[1], use_paddle=True)
        str = " ".join(list(str_list))
        res = temp[0] + '\t' + str + '\n'
        f1.writelines(res)

f1.close()

