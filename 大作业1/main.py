import pickle
from Dictionary_PTCP import d_ptcp
from Statistics_PTCP import s_ptcp
from Analysis import analysis

with open("Statistics/prob/probs.p", "rb") as f:
    probs = pickle.load(f)
with open("Dictionary/Dict/dict.p", "rb") as f:
    dic = pickle.load(f)

with open("File/test_data.txt","r",encoding='utf-8') as f:
    f1 = open("Dictionary/Dictionary_out.txt","w+",encoding='utf-8')
    f2 = open("Statistics/Statistics_out.txt", "w+", encoding='utf-8')
    for line in f:
        f1.writelines(d_ptcp(line,dic,True))
        f2.writelines(s_ptcp(line,probs))
    f1.close()
    f2.close()

analysis("Dictionary/Dictionary_out.txt")
analysis("Statistics/Statistics_out.txt")
