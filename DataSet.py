import numpy as np
import pickle
from collections import defaultdict

def dataset():
    dic = {
        "m": 0,
        "a": 1,
        "vt": 2,
        "d": 3,
        "ad": 4,
        "qt": 5,
        "n": 6,
        "f": 7,
        "vq": 8,
        "vn": 9,
        "vi": 10,
        "dc": 11
    }
    transmat = np.zeros((len(dic), len(dic)))
    word_list = defaultdict(dict)
    speech_list = defaultdict(int)

    file_name = "Data.txt"
    f = open(file_name, "r", encoding='utf-8')
    data = f.read()
    f.close()
    x = data.split()

    father = False
    father_word = None
    for i in x:
        word = i.split("/")

        if word[1] in dic.keys():
            if father:
                transmat[dic[father_word], dic[word[1]]] += 1
            father = True
            father_word = word[1]
        else:
            father = False

        if word[1] in word_list[word[0]].keys():
            word_list[word[0]][word[1]] += 1
        else:
            word_list[word[0]][word[1]] = 1

        speech_list[word[1]] += 1

    # dic 词性 transmat 词性转移矩阵 word_list 词的词性表
    return dic, transmat, word_list, speech_list


dic, transmat, word_list, speech_list= dataset()
f = open("varname.txt","wb")
varname = {
    "dic": dic,
    "transmat": transmat,
    "word_list": word_list,
    "speech_list": speech_list
}
pickle.dump(varname,f)
f.close()
