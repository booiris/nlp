import pickle
import string

f = open("varname.txt", "rb")
varname = pickle.load(f)
dic = varname["dic"]
transmat = varname["transmat"]
word_list = varname["word_list"]
speech_list = varname["speech_list"]

punc = string.punctuation

cnt1 = 0
cnt2 = 0
for word in word_list:
    if len(word_list[word]) == 1:
        flag = True
        for i in word:
            if i in punc:
                flag = False
                break
        if flag:
            cnt1 += 1

    else:
        temp = sorted(word_list[word].items(), key=lambda item: item[1], reverse=True)
        word_list[word] = dict(temp)
        cnt2 += 1

print("非兼类词数量:",cnt1)
print("兼类词数量:",cnt2)
print("想法:",word_list["想法"])
print("要求:",word_list["要求"])
